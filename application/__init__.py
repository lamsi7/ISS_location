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
        from .plotlydash.dash_2d import init_dashboard_2d
        app = init_dashboard(app)
        app_2d = init_dashboard_2d(app)
    return app, app_2d

# def init_app_2d():
#     """Construct core Flask application with embedded Dash app."""
#     app = Flask(__name__)
#     with app.app_context():
#         # Import parts of our core Flask app
#         from . import routes

#         # Import Dash application
#         from .plotlydash.dashboard import init_dashboard
#         app = init_dashboard(app)
#     return app