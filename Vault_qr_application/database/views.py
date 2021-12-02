""" A temporary database blueprint for my CS220 project
"""

from flask import Blueprint
from flask import current_app as app
from flask import render_template
from flask import request

from CRUD import get_results

# Blueprint Configuration
db_bp = Blueprint(
    'db_bp', __name__,
    template_folder='templates',
    static_folder='static'
)



@db_bp.route('/search', methods=['GET','POST'])
def search():
    """ serve the about page. Consider migrating routing to /about in the future when
    more pages are added
    """
    get_current_results()
    if request.method == 'POST':
        get_current_results(None, request.form['user_search'])
    
    return render_template("database/search.html", results=current_results)


def get_current_results(result_type=None, search_string=None):
    global current_results 
    current_results = get_results(result_type, search_string)
    return current_results