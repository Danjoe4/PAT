""" An error handling file for the entire app. Should handle primarily 404 and 405 exceptions,
which are not invoked in the context of a blueprint. Also handles database errors as well
"""

from flask import Flask, render_template, redirect


def handle_error_404(e):
    """ Redirects our user to the home page if they attempt to visit any non-existent url 
    """
    # if request.path.startswith('/api/') consider adding
    return redirect("/home", code=302)

