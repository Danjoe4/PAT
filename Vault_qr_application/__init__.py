""" Initializes the Flask app and registers the appropriate blueprints. The top-level entry
point of our application
"""
from flask import Flask


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.DevConfig")

    with app.app_context():
        # load the configuration values from env variables
        # import ..config
        # app.config.from_object('config.DevConfig') 

        # logging, add

        # set up the database
        """
        from .database.connect import db_session
        @app.teardown_appcontext
        def shutdown_session(exception=None):
            db_session.remove()"""

        # Import parts of our application
        from .home.views import home_bp
        from .scan.views import scan_bp
        from .extra.views import extra_bp
        from .database.views import db_bp
        # Register Blueprints
        app.register_blueprint(home_bp, url_prefix='/home')
        app.register_blueprint(scan_bp, url_prefix='/scan')
        app.register_blueprint(extra_bp, url_prefix='/extra')
        app.register_blueprint(db_bp, url_prefix='/database')

        # Import and register APPLICATION error handlers
        from .error import handle_error_404
        app.register_error_handler(404, handle_error_404)

        print(app.url_map)

        return app