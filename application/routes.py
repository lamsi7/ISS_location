"""Routes for parent Flask app."""
from flask import render_template
from flask import current_app as app


@app.route('/')
def home():
    """Landing page."""
    return render_template('home.html')


@app.route('/test')
def d():
    return render_template('d.html')
