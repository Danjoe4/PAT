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


############ useful globals; same for all users ################################3
# load our yaml file with all our secrets
with open("config.yaml") as f_stream:
    config_file = yaml.load(f_stream, yaml.FullLoader)
# set the private key and account address
private_key = config_file["private_key"]
account_address = config_file["account_address"]

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
    session['serial'] = str(request.args.get('serial'))
    session['product'] = str(request.args.get('product'))
    session['brand'] = str(request.args.get('brand'))


    return serve_loading_page()
    # contract_address16 = deploy_contract(serial, product, brand)

    #return serial
    #return f"success! Here is the contract location (bech16 address): {contract_address16}"


def serve_loading_page():
    # this template fetches deploy_contract() while displaying a loading screen,
    # then redirects to the results page
    return render_template('loading.html')


@app.route("/results")
def serve_results_page():
    # pull saved values from the session
    print(session)
    return session

    #return render_template('results.html', data=session)


@app.route("/deploy")
def deploy_contract():
    # create the contract from file
    code = open("contract.scilla").read()
    contract = Contract.new_from_code(code)

    contract.account = account # set the account

    # set custom initialization variables and deploy
    init = set_init(session['serial'], session['product'], session['brand'])
    contract.deploy(init_params = init)
    assert contract.status == Contract.Status.Deployed

    # add the contract address
    session['contract_address'] = zilkey.to_bech32_address(contract.address)
    return session # now the js file has the info it needs


def set_init(serial, product, brand):
    today = date.today()
    d1 = today.strftime("%m/%d/%y")

    return [
    Contract.value_dict("_scilla_version", "Uint32", "0"),
    Contract.value_dict("serial_number", "String", serial),
    Contract.value_dict("owner", "ByStr20", account.address0x),
    Contract.value_dict("print_date", "String", d1),
    Contract.value_dict("product", "String", product),
    Contract.value_dict("brand", "String", brand)
    ]



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    #deploy_contract("TESTV0_2", "Headphones", "BOSE")