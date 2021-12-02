""" view for extra templates"""

from flask import Blueprint
from flask import current_app as app
from flask import render_template

# Blueprint Configuration
extra_bp = Blueprint(
    'extra_bp', __name__,
    template_folder='templates',
    static_folder='static'
    # consider alternative folder hierarchy or different jinja2 loader
)

@extra_bp.route('/category', methods=['GET'])
def serve_category_page():
    return render_template("extra/category.html")

@extra_bp.route('/login', methods=['GET'])
def serve_login_page():
    return render_template("extra/login.html")

@extra_bp.route('/storage', methods=['GET'])
def serve_storage_page():
    return render_template("extra/storage.html")