"""Routes for parent Flask app."""
from flask import render_template
from flask import current_app as app


@app.route('/')
def home():
    """Landing page."""
    return render_template('home.html')


@app.route('/frame_3d_iss/')
def dash_frame():
    return render_template('dash_flask.html')

@app.route('/plotly_ISS_2D/')
def plotly_iss_2d():
    return render_template('plotly_2d.html')

@app.route('/test/')
def test_iss_2d():
    return render_template('test_2d.html')