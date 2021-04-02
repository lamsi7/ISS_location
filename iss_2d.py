import json

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline
import numpy as np

# plot ISS
data = [Scattergeo(lon=np.array(176.6897), lat=np.array(-49.6460))]
my_layout = Layout(title='Test')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='test_2d.html')
