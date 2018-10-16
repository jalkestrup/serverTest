from flask import render_template
from app import app,db

@app.errorhandler(500)
def not_found_error(error):
    return render_template('500.html'), 500