import json

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline
import numpy as np
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
import dash
import sys
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from application import coor

def init_dashboard_2d(server):
        # CSS
    external_stylesheets = [
        'https://codepen.io/chriddyp/pen/bWLwgP.css']
    # Set dash
    dash_app_2d = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp_2d/',
        external_stylesheets=external_stylesheets,
        title='ISS - 2D visualization'
    )
    dash_app_2d.layout = html.Div(
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
    init_callbacks(dash_app_2d)
    return dash_app_2d.server

def init_callbacks(dash_app_2d):
    # Text live update
    @dash_app_2d.callback(Output('live-update-text', 'children'),
                       Input('interval-component', 'n_intervals'))
    def update_metrics(n):
        iss_location = coor.iss_req()
        iss_lat = iss_location['latitude']
        iss_lon = iss_location['longitude']
        style = {'padding': '5px', 'fontSize': '16px'}
        return [
            html.Span('Longitude: {}'.format(iss_lon), style=style),
            html.Span('Latitude: {}'.format(iss_lat), style=style),
        ]
    # For live update of graph:
    @dash_app_2d.callback(Output('iss-graph', 'figure'), Input('interval-component', 'n_intervals'))
    def iss_2d(n):
        # ISS
        iss_location = coor.iss_req()

        # Will retrieve string but it will be converted in mapping_map_to_sphere
        iss_lat = np.array(float(iss_location['latitude']))
        iss_lon = np.array(float(iss_location['longitude']))

        plot_data_iss = [Scattergeo(lon=iss_lon, lat=iss_lat, mode='markers', text='ISS',marker=dict(color = 'rgb(255,0,0)',size=13))]

        my_layout = Layout(paper_bgcolor='rgb(64,64,64)', plot_bgcolor='rgb(64,64,64)', height=800)

        fig = go.Figure(data=plot_data_iss, layout=my_layout)

        #Change default layout
        fig.update_layout(geo = dict(
        landcolor = "rgb(212, 212, 212)",
        subunitcolor = "rgb(255, 255, 255)",
        countrycolor = "rgb(255, 255, 255)"), margin={"r":0,"t":0,"l":0,"b":30}
        )
        return fig
