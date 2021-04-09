from flask import Flask
from .plotlydash.dashboard import init_dashboard


def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__)
    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        # Import Dash application
        from .plotlydash.dashboard import init_dashboard
        app = init_dashboard(app)
    return app
