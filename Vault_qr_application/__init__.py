""" Initializes the Flask app and registers the appropriate blueprints. The top-level entry
point of our application
"""
from flask import Flask


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.DevConfig")

    with app.app_context():
        # logging, add

        # set up the database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/vault'

        # Import parts of our application
        from .home.views import home_bp
        from .scan.views import scan_bp

        # Register Blueprints
        app.register_blueprint(home_bp, url_prefix='/home')
        app.register_blueprint(scan_bp, url_prefix='/scan')

        # Import and register APPLICATION error handlers
        from .error import handle_error_404
        app.register_error_handler(404, handle_error_404)

        print(app.url_map)

        return app