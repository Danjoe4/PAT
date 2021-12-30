import datetime
from os import environ

from pyzil.crypto import zilkey
from pyzil.zilliqa import chain
from pyzil.zilliqa.units import Zil, Qa
from pyzil.account import Account, BatchTransfer
from pyzil.contract import Contract


def mint_nft(user_query: dict) -> zilkey:
    """ Mint the contract and return the contract address
    """
    code = open("Vault_qr_application/scan/contract.scilla").read()
    contract = Contract.new_from_code(code)
    account = Account(address = environ.get('ZIL_WALLET_ACCOUNT_ADDRESS'), 
    private_key = environ.get('ZIL_WALLET_PRIVATE_KEY')) 
    contract.account = account
    # set custom initialization variables and deploy #change gas price
    contract.deploy(init_params = init_nft_params(user_query, account), gas_price = 6000000000) 
    assert contract.status == Contract.Status.Deployed #hmmmm this fails
    contract_address = zilkey.to_bech32_address(contract.address)
    
    return contract_address


def init_nft_params(user_query: dict, account):
    return [
    Contract.value_dict("brand", "String", user_query['brand']),
    Contract.value_dict("product", "String", user_query['product']),
    Contract.value_dict("model", "String", user_query['model']),
    Contract.value_dict("serial", "String", user_query['serial']),
    Contract.value_dict("print_date", "String", init_date_str()),
    Contract.value_dict("owner", "ByStr20", account.address0x),
    Contract.value_dict("_scilla_version", "Uint32", "0")
    ]


def init_date_str():
    today = datetime.datetime.utcnow()
    d1 = today.strftime("%b %d %Y %H:%M:%S")
    return d1

def get_current_chain():
    CURRENT_CHAIN = environ.get('ZIL_ACTIVE_CHAIN')
    chain.set_active_chain(chain.TestNet)
    return CURRENT_CHAIN