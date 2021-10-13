""" Initializes the Flask app and registers the appropriate blueprints. The top-level entry
point of our application
"""
from flask import Flask


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.DevConfig")

    with app.app_context():
        # Import parts of our application
        from .home.views import home_bp
        #from .scan.views import scan_bp

        # Register Blueprints
        app.register_blueprint(home_bp, url_prefix='/home')
        #app.register_blueprint(scan_bp, url_prefix='/scan')


        print(app.url_map)

        return app