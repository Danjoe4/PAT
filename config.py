"""App configuration. Use r'string' format for strings with weird characters. Run this file 
to set all the config values to the environment. Not called by the app.
Flask configurations are all caps. Secrets are lower case"""

import os


Config = {
'SECRET_KEY' : r'\x91x\xad{\xfbh[A<\x86\xc4\xc6\x8a\x89\x1e\x8a#\xef\xa8f\x06\xb5\xa5\x0b\xc7\x83t\x88\xdf@\xedh',
'STATIC_FOLDER' : 'static',
'TEMPLATES_FOLDER' : 'templates',
# Zilpay account info
'private_key': 'ee3c7649edbf89807b2ca1b682fe43f9b917cd673d82ba6668468a6a9bec81fe',
'account_address': '0x64E97Af0a1702C40a2e610A8d66d9BeDd7C08fDA',
# for decrypting the url, should not be exposed like this
'encryption_password_1': 'password',
'encryption_salt_1': r'\xb7\x01\x0b\x03Y\xc4\xe7\xa6\r\xbd\x1d\xb4;iD\xfd',
}
DevConfig = {
'FLASK_ENV' : 'development',
'TESTING' : 'true',

# other helpful stuff
'EXPLAIN_TEMPLATE_LOADING' : 'true',

# Flask-Session 
'SESSION_PERMANENT' : 'false',
'SESSION_TYPE' : 'filesystem',
'PERMANENT_SESSION_LIFETIME' : '60', # the session lasts 60 seconds
}


def set_config_to_env(config_type): 
    """ Save the base Config and the Dev/Prod/Staging/Testing/etc config to the env variables as a dict
    """
    assert config_type in globals()
    if config_type == "DevConfig":
        d = {**Config, **DevConfig}
        os.environ['APPLICATION_SETTINGS'] = str(d)
    return

def update_config_value(key, val):
    """ Useful if you have a highly customized config and want to preserve previous changes
    """
    config_dict = dict(os.environ['APPLICATION_SETTINGS'])
    config_dict[key] = val
    os.environ['APPLICATION_SETTINGS'] = str(config_dict)
    return


if __name__ == "__main__":
    set_config_to_env("DevConfig")