from flask import Flask, request, render_template, session
from flask_session import Session


from pyzil.crypto import zilkey
from pyzil.zilliqa import chain
from pyzil.zilliqa.units import Zil, Qa
from pyzil.account import Account, BatchTransfer
from pyzil.contract import Contract

from datetime import date
import time as t
import yaml
import csv
import zlib
from base64 import urlsafe_b64decode


############ useful globals; same for all users ################################
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
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config.from_object(__name__)
Session(app)

############################################################################

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/send')
def main():
    # gather values from the POST request and save to the session
    encoded_value = request.args.get('v')
    print(encoded_value)

    params_list = unobscure(encoded_value)
    print(params_list)

    # save these params to the session
    session['brand'] = str(params_list[0])
    session['product'] = str(params_list[1])
    session['model'] = str(params_list[2])
    session['serial'] = str(params_list[3])
    print(session)

    return serve_loading_page()




def serve_loading_page():
    # this template fetches deploy_contract() while displaying a loading screen,
    # then redirects to the results page
    return render_template('loading.html')


@app.route("/results")
def serve_results_page():
    # pull saved values from the session
    print(session)
    print(session['contract_address'])
    data = {
        'product_page' : get_product_page(),
        'viewblock_page' : get_viewblock_page()
    }

    return render_template('results.html', data=data)


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


def get_viewblock_page():
    # string format should be the same every time
    addr = session['contract_address']
    return f"https://viewblock.io/zilliqa/address/{addr}?network={CURRENT_CHAIN}&tab=state"


@app.route("/deploy")
def deploy_contract():

    # create the contract from file
    code = open("contract.scilla").read()
    contract = Contract.new_from_code(code)

    contract.account = account # set the account

    # set custom initialization variables and deploy
    contract.deploy(init_params = set_init(), gas_price = 6000000000) #add gas price
    assert contract.status == Contract.Status.Deployed #hmmmm this fails

    # add the contract address to the session
    session['contract_address'] = zilkey.to_bech32_address(contract.address)
    
    # fetch() requires that this function return a json, but 
    return {} # we're using a server side session instead


def set_init():
    today = date.today()
    d1 = today.strftime("%m/%d/%y")

    return [
    Contract.value_dict("brand", "String", session['brand']),
    Contract.value_dict("product", "String", session['product']),
    Contract.value_dict("model", "String", session['model']),
    Contract.value_dict("serial", "String", session['serial']),
    Contract.value_dict("owner", "ByStr20", account.address0x),
    Contract.value_dict("print_date", "String", d1),
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


if __name__ == "__main__":
    #unobscure(b'eNpL0UlJASIwTgEAHekEbQ==')
    app.run(debug=True)
    #deploy_contract("TESTV0_2", "Headphones", "BOSE")
    #unobscure(http://127.0.0.1:5000/send?v=b%27eNqLdsovTtXxcHV0CfDw93MN1jFzcfLRCfb3dQ12DfJ09DEyMTI2NTOPBQDvFwsO%27")