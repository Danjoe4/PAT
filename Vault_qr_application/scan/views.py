
from flask import Blueprint
from flask import current_app as app
from flask import render_template, request, session, jsonify
from flask_session import Session 

import binascii # handles an error from modifying the url, may be deprecated 
import zlib
import csv

from .query import Query
from .mint import mint_nft, get_current_chain

# Blueprint Configuration
scan_bp = Blueprint(
    'scan_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@scan_bp.route('/', methods=['GET', 'POST'])
def main():
    """ Called when the QR code is scanned. Gathers values from the POST request 
    and decides what to do with them
    """
    user_query = Query(request.args.get('v'))
    print(user_query)

    ##### change once db is added ############################################
    existing_urls = check_for_dup(user_query.encrypted_str)
    #print("the existing urls:")
    #print(existing_urls)
    # check if the QR has been scanned already
    if existing_urls is not False:
        session["product_page"] = existing_urls[0]
        session["viewblock_page"] = existing_urls[1]
        return render_template("scan/duplicate_loading.html")
    ########################################################################

    # otherwise proceed to generate the NFT as normal
    try: # catches error caused by the user modifying the url string
        session["user_query"] = user_query.__dict__ # custom types must be stored as a dict
    except (binascii.Error, zlib.error) as err: 
        return render_template("scan/error.html") ##add bp error handler

    return serve_loading_page()


@scan_bp.route('/duplicate')
def serve_duplicate_page():
    data={"product_page":  session["product_page"],
        "viewblock_page": session["viewblock_page"]
        }
    return render_template("scan/already_scanned.html", data=data)


@scan_bp.route("/deploy")
def deploy_contract():
    """ Uses pyzil to deploy the contract
    """
    # create the contract from the user query, store its address
    session["contract_address"] = mint_nft(session["user_query"])

    # fetch() requires that this function return a json, but 
    return {} # we're using a server side session instead


@scan_bp.route("/results")
def serve_results_page():
    # pull saved values from the session
    print("/results session values: ")
    
    
    product_page = get_product_page(session['user_query']['model'])
    viewblock_page = get_viewblock_page(session['contract_address'])

    #temp duplication solution
    add_entry(session['user_query']['encrypted_str'], product_page, viewblock_page)

    return render_template('scan/results.html', data={
        'product_page' : product_page,
        'viewblock_page' : viewblock_page
    })


@scan_bp.route("/deploying")
def return_cookie():
    """ This is only to return a cookie to the fetch in duplicate_loading.js because HTTP is stateless
    """
    return {}






def serve_loading_page():
    # this template fetches deploy_contract() while displaying a loading screen,
    # then redirects to the results page
    return render_template('scan/loading.html')


def get_product_page(model):
    # open our database
    csv_file = csv.reader(open('Vault_qr_application/scan/database.csv', "r"), delimiter=",")
    url = None
    for row in csv_file: #look for the model number
        if model == row[1]:
            url = row[2]
    
    if url is None: # fail safe
        url = 'https://www.bose.com/en_us/index.html'

    return url


def get_viewblock_page(addr):
    # string format should be the same every time
    return f"https://viewblock.io/zilliqa/address/{addr}?network={get_current_chain()}&tab=state"





################# SOON TO BE DEPRECATED ######################################
def check_for_dup(encoded_value):
    """ Returns [product_page, viewblock_page] if the database contains the same encoded string,
    """
    # open our database
    with open('Vault_qr_application/scan/dup_checker.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader: #look for the value
            if encoded_value == row[0]:
                return [row[1], row[2]]
    
    return False



def add_entry(enc_val, product_url, viewblock_url):
    with open("dup_checker.csv", 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow([enc_val, product_url, viewblock_url])
############################################################################################
