"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
print(basedir)

import yaml # bad practice; in the future we should save our keys as ENV vars. For example:
# environ.get('SECRET_KEY')

class Config:
    """Base config """
    with open("config.yaml") as f_stream:
        config_file = yaml.load(f_stream, yaml.FullLoader)

    SECRET_KEY = config_file["flask_session_key"]
    # SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

#########################
#class ProdConfig(Config):
#    FLASK_ENV = 'production'
#    DEBUG = False
#    TESTING = False
#    DATABASE_URI = environ.get('PROD_DATABASE_URI')
##########################

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    # DATABASE_URI = environ.get('DEV_DATABASE_URI')

    # other helpful stuff
    EXPLAIN_TEMPLATE_LOADING = True

    # Flask-Session config 
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    PERMANENT_SESSION_LIFETIME = 60 # the session lasts 60 seconds