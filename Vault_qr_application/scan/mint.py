import time
import datetime
import yaml

from pyzil.crypto import zilkey
from pyzil.zilliqa import chain
from pyzil.zilliqa.units import Zil, Qa
from pyzil.account import Account, BatchTransfer
from pyzil.contract import Contract

#### Dangerous Globals! #############
# load our yaml file with all our secrets
with open("config.yaml") as f_stream:
    config_file = yaml.load(f_stream, yaml.FullLoader)
# set the private key and account address
private_key = config_file["private_key"]
account_address = config_file["account_address"]
CURRENT_CHAIN = "testnet"
chain.set_active_chain(chain.TestNet)
account = Account(address = account_address, private_key = private_key)
###########################

def mint_nft(user_query) -> zilkey:
    """ Mint the contract and return the contract address
    """
    code = open("contract.scilla").read()
    contract = Contract.new_from_code(code)
    contract.account = account 
    # set custom initialization variables and deploy
    contract.deploy(init_params = init_nft_params(user_query), gas_price = 6000000000) #change gas price
    assert contract.status == Contract.Status.Deployed #hmmmm this fails

    contract_address = zilkey.to_bech32_address(contract.address)
    return contract_address


def init_nft_params(user_query):
    return [
    Contract.value_dict("brand", "String", user_query.brand),
    Contract.value_dict("product", "String", user_query.product),
    Contract.value_dict("model", "String", user_query.model),
    Contract.value_dict("serial", "String", user_query.serial),
    Contract.value_dict("print_date", "String", init_date_str()),
    Contract.value_dict("owner", "ByStr20", account.address0x),
    Contract.value_dict("_scilla_version", "Uint32", "0")
    ]


def init_date_str():
    today = datetime.datetime.utcnow()
    d1 = today.strftime("%b %d %Y %H:%M:%S")
    return d1