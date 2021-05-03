import json

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline
import numpy as np
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
import dash
from plotly.offline import plot
import sys
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from application import coor

## plot ISS
# data = [Scattergeo(lon=np.array(176.6897), lat=np.array(-49.6460))]
# my_layout = Layout(title='2D visualization')

# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='test_2d.html')

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
        print("Updating 2D")
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

        plot_data_iss = [Scattergeo(lon=iss_lon, lat=iss_lat)]

        my_layout = Layout(title='2D visualization',paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=800)

        fig = go.Figure(data=plot_data_iss, layout=my_layout)
        #fig.update_traces(lon=iss_lon, lat=iss_lat, visible= True, selector=dict(type='scattergeo'))
        #fig = {'data': data, 'layout': my_layout}
        #fig.update_layout(scene=scene)
        return fig
