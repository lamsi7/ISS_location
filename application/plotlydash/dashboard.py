import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
import dash
from plotly.offline import plot
import sys
import plotly.graph_objs as go
import numpy as np
from dash.dependencies import Input, Output
from application import coor
from application import earth_3d as earth

"""
Let the ISS location be updated every 5 seconds -> plotly dash
"""


def init_dashboard(server):
    # CSS
    external_stylesheets = [
        'https://codepen.io/chriddyp/pen/bWLwgP.css']
    # Set dash
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=external_stylesheets,
        title='ISS 3D'
    )
    #dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    # Layout; interval - 5 sec
    dash_app.layout = html.Div(
        html.Div([
            #dcc.Link('Go back to the main page.', href='/'),
            html.H4('ISS Live Feed Updated Every 5 seconds', style={'color':'white'}),
            html.Div(id='live-update-text', style={'color':'white'}),
            dcc.Graph(id='iss-graph'),
            dcc.Interval(
                id='interval-component',
                interval=5*1000,  # in milliseconds
                n_intervals=0
            )
        ])
    )
    init_callbacks(dash_app)
    return dash_app.server


"""Callbacks:"""


def init_callbacks(dash_app):
    # Text live update
    @dash_app.callback(Output('live-update-text', 'children'),
                       Input('interval-component', 'n_intervals'))
    def update_metrics(n):
        print("Updating 3D")
        iss_location = coor.iss_req()
        iss_lat = iss_location['latitude']
        iss_lon = iss_location['longitude']
        style = {'padding': '5px', 'fontSize': '16px'}
        return [
            html.Span('Longitude: {}'.format(iss_lon), style=style),
            html.Span('Latitude: {}'.format(iss_lat), style=style),
        ]

    # For live update of graph:
    @dash_app.callback(Output('iss-graph', 'figure'), Input('interval-component', 'n_intervals'))
    def iss(n):
        # ISS
        iss_location = coor.iss_req()

        # Will retrieve string but it will be converted in mapping_map_to_sphere
        iss_lat = iss_location['latitude']
        iss_lon = iss_location['longitude']

        # Convert to spherical coordinates
        xs_ev_org, ys_ev_org, zs_ev_org = earth.mapping_map_to_sphere(
            iss_lon, iss_lat)
        x_iss = np.array(xs_ev_org)
        y_iss = np.array(ys_ev_org)
        z_iss = np.array(zs_ev_org*1.1)
        iss_scatter = go.Scatter3d(x=x_iss,
                                   y=y_iss,
                                   z=z_iss,
                                   mode='markers',
                                   name='ISS'
                                   )

        plot_data_iss = [earth.topo_sphere]+[iss_scatter]

        # After loading set the view where the ISS is located
        scene = dict(camera=dict(eye=dict(x=xs_ev_org*1.5,
                                          y=ys_ev_org*1.5, z=zs_ev_org*1.5)))
        fig = go.Figure(data=plot_data_iss, layout=earth.layout)
        fig.update_layout(scene=scene)
        return fig
