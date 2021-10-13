
from flask import Blueprint
from flask import current_app as app
from flask import render_template

# Blueprint Configuration
scan_bp = Blueprint(
    'about_bp', __name__,
    template_folder='templates/scan',
    static_folder='static/scan'
    # consider alternative folder hierarchy or different jinja2 loader
)


@scan_bp.route('/', methods=['GET'])
def about():
    """ serve the about page
    """
    return render_template("scan.html")