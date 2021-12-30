""" The web host has its own (different) WSGI file which initializes the app. 
You should run this one for local testing. This is a useful abstraction because 
the only file that is different on the webhost is the wsgi. The web host file
has several pathing variables set, plus the following two lines:

from Vault_qr_application import init_app
application = init_app()
"""

from Vault_qr_application import init_app


app = init_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    #unobscure(b'eNpL0UlJASIwTgEAHekEbQ==')
    #app.run(debug=True)
    #deploy_contract("TESTV0_2", "Headphones", "BOSE")
    #unobscure(http://127.0.0.1:5000/send?v=b%27eNqLdsovTtXxcHV0CfDw93MN1jFzcfLRCfb3dQ12DfJ09DEyMTI2NTOPBQDvFwsO%27")
    #print(init_date_str())