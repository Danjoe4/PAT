""" Define our home blueprint and its routes.
"""

from flask import Blueprint
from flask import current_app as app
from flask import render_template

# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
    # consider alternative folder hierarchy or different jinja2 loader
)



@home_bp.route('/', methods=['GET'])
def about():
    """ serve the about page. Consider migrating routing to /about in the future when
    more pages are added
    """
    return render_template("home/about.html")


