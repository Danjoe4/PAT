""" Initializes the Flask app and registers the appropriate blueprints. The top-level entry
point of our application
"""
from flask import Flask


def init_app():
    """Initialize the core application."""
    # logging is a must, especially while the app is being built, consider moving this tho
    import logging
    logging.basicConfig(filename='debug_log.log', level=logging.DEBUG)

    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_object("config.DevConfig")
    # load the configuration values from a dict with env variables
    app.config.from_object(FlaskConfig)
    
    logging.debug(app.config)

    with app.app_context():
        # set up the database
        

        # Import parts of our application
        from .home.views import home_bp
        from .scan.views import scan_bp
        from .extra.views import extra_bp
        # Register Blueprints
        app.register_blueprint(home_bp, url_prefix='/home')
        app.register_blueprint(scan_bp, url_prefix='/scan')
        app.register_blueprint(extra_bp, url_prefix='/extra')

        # Import and register APPLICATION error handlers
        from .error import handle_error_404
        app.register_error_handler(404, handle_error_404)

        print(app.url_map)

        return app



class FlaskConfig:
    """Load the flask configuration values into a dict from env variables"""
    from os import environ
    from dotenv import load_dotenv
    load_dotenv()
    
    SECRET_KEY = environ.get('FLASK_SECRET_KEY')
    STATIC_FOLDER = environ.get('FLASK_STATIC_FOLDER')
    TEMPLATES_FOLDER = environ.get('FLASK_TEMPLATES_FOLDER')
    FLASK_ENV = environ.get('FLASK_FLASK_ENV')
    TESTING = environ.get('FLASK_TESTING')

    # Flask-Session 
    SESSION_PERMANENT = environ.get('FLASK_SESSION_PERMANENT')
    SESSION_TYPE = environ.get('FLASK_SESSION_TYPE')
    PERMANENT_SESSION_LIFETIME = environ.get('FLASK_PERMANENT_SESSION_LIFETIME')

    # other helpful stuff
    EXPLAIN_TEMPLATE_LOADING = environ.get('FLASK_EXPLAIN_TEMPLATE_LOADING')