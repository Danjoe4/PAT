from flask import Flask, request, render_template, session, jsonify
from flask_session import Session 

from pyzil.crypto import zilkey
from pyzil.zilliqa import chain
from pyzil.zilliqa.units import Zil, Qa
from pyzil.account import Account, BatchTransfer
from pyzil.contract import Contract

import time
import datetime
import yaml
import csv
import zlib
from base64 import urlsafe_b64decode
import binascii

############ useful globals; same for all users ###########################
# load our yaml file with all our secrets
with open("config.yaml") as f_stream:
    config_file = yaml.load(f_stream, yaml.FullLoader)
# set the private key and account address
private_key = config_file["private_key"]
account_address = config_file["account_address"]

CURRENT_CHAIN = "testnet"
chain.set_active_chain(chain.TestNet)
account = Account(address = account_address, private_key = private_key)


app = Flask(__name__, 
static_folder='static',
template_folder='templates')

# for the session, i.e passing values
app.secret_key = config_file["flask_session_key"]
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["PERMANENT_SESSION_LIFETIME"] = 60 # the session lasts 60 seconds
app.config.from_object(__name__)
Session(app)

############################################################################

@app.route('/')
def index():
    """ root page, this is good for testing, although we should eventually turn it
    into an about page or something
    """
    #return render_template("loading.html")
<<<<<<< HEAD
    return render_template("home.html")
=======
    #return render_template("home.html")
>>>>>>> f6b819f16c0faff256f7e191e04c4f65cad0b2c4
    #return render_template("duplicate_loading.html")


@app.route('/send')
def main():
    """ Called when the QR code is scanned. Gathers values from the POST request 
    and decides what to do with them
    """
    encoded_value = request.args.get('v')
    print("initial val:")
    print(encoded_value)

    # check if the QR has been scanned already
    existing_urls = check_for_dup(encoded_value)
    print("the existing urls:")
    print(existing_urls)
    if existing_urls is not False:
        session["product_page"] = existing_urls[0]
        session["viewblock_page"] = existing_urls[1]
        return render_template("duplicate_loading.html")

    # otherwise proceed to generate the NFT as normal
    try: # catches error caused by the user modifying the url string
        save_product_parameters_to_session(encoded_value)
    except (binascii.Error, zlib.error) as err: 
        return render_template("error.html")

    return serve_loading_page()


@app.route('/duplicate')
def serve_duplicate_page():
    data={"product_page":  session["product_page"],
        "viewblock_page": session["viewblock_page"]
        }
    return render_template("already_scanned.html", data=data)


@app.route("/deploy")
def deploy_contract():
    """ Uses pyzil to deploy the contract
    """
    # create the contract from file
    code = open("contract.scilla").read()
    contract = Contract.new_from_code(code)
    contract.account = account # set the account

    # set custom initialization variables and deploy
    contract.deploy(init_params = set_init(), gas_price = 6000000000) #add gas price
    assert contract.status == Contract.Status.Deployed #hmmmm this fails

    # add the contract address to the session
    session['contract_address'] = zilkey.to_bech32_address(contract.address)
    print(session)

    # fetch() requires that this function return a json, but 
    return {} # we're using a server side session instead


@app.route("/results")
def serve_results_page():
    # pull saved values from the session
    print("/results session values: ")
    print(session)
    product_page = get_product_page()
    viewblock_page = get_viewblock_page(session['contract_address'])

    #temp duplication solution
    add_entry(session['encoded_value'], product_page, viewblock_page)

    return render_template('results.html', data={
        'product_page' : product_page,
        'viewblock_page' : viewblock_page
    })


@app.route("/deploying")
def return_cookie():
    """ This is only to return a cookie to the fetch in duplicate_loading.js
    """
    return {}




def save_product_parameters_to_session(encoded_value):
    session['encoded_value'] = encoded_value
    params_list = unobscure(encoded_value)
    print(params_list)

    # save these params to the session
    session['brand'] = str(params_list[0])
    session['product'] = str(params_list[1])
    session['model'] = str(params_list[2])
    session['serial'] = str(params_list[3])
    #print(session)




def serve_loading_page():
    # this template fetches deploy_contract() while displaying a loading screen,
    # then redirects to the results page
    return render_template('loading.html')


def get_product_page():
    # open our database
    csv_file = csv.reader(open('database.csv', "r"), delimiter=",")
    url = None
    for row in csv_file: #look for the model number
        if session['model'] == row[1]:
            url = row[2]
    
    if url is None: # fail safe
        url = 'https://www.bose.com/en_us/index.html'

    return url


def get_viewblock_page(addr):
    # string format should be the same every time
    return f"https://viewblock.io/zilliqa/address/{addr}?network={CURRENT_CHAIN}&tab=state"




def set_init():
    return [
    Contract.value_dict("brand", "String", session['brand']),
    Contract.value_dict("product", "String", session['product']),
    Contract.value_dict("model", "String", session['model']),
    Contract.value_dict("serial", "String", session['serial']),
    Contract.value_dict("print_date", "String", init_date_str()),
    Contract.value_dict("owner", "ByStr20", account.address0x),
    Contract.value_dict("_scilla_version", "Uint32", "0")
    ]


def unobscure(obscured: bytes) -> list:
    """ For testing, decodes from base64, decompresses, then decodes back 
    to a regular string and splits into a list
    """
    # we need to chop off b'..' because .get() returns a string

    out = zlib.decompress(urlsafe_b64decode(obscured))
    out = out.decode('utf-8').split(',')
    print(out)
    return out


def check_for_dup(encoded_value):
    """ Returns [product_page, viewblock_page] if the database contains the same encoded string
    """
    # open our database
    with open('dup_checker.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader: #look for the value
            print(row)
            if encoded_value == row[0]:
                return [row[1], row[2]]
    
    return False



def add_entry(enc_val, product_url, viewblock_url):
    with open("dup_checker.csv", 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow([enc_val, product_url, viewblock_url])


def init_date_str():
    today = datetime.datetime.utcnow()
    d1 = today.strftime("%b %d %Y %H:%M:%S")
    return d1


if __name__ == "__main__":
    #unobscure(b'eNpL0UlJASIwTgEAHekEbQ==')
    app.run(debug=True)
    #deploy_contract("TESTV0_2", "Headphones", "BOSE")
    #unobscure(http://127.0.0.1:5000/send?v=b%27eNqLdsovTtXxcHV0CfDw93MN1jFzcfLRCfb3dQ12DfJ09DEyMTI2NTOPBQDvFwsO%27")
    #print(init_date_str())