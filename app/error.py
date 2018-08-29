from flask import render_template
from app import app

@app.errorhandler(404)
def four_ow_four(error):
    """
    Function to render the 404 error page
    :param error:
    :return:
    """

    return render_template('fourowfour.html'), 404
