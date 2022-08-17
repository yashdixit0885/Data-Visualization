
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data

filename = 'Data Visualization/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    

readable_file = 'Data Visualization/data/readable_eq_data.json'

with open(readable_file, 'w') as f:
    json.dump(all_eq_data,f,indent=4)

all_eq_dicts = all_eq_data['features']

mags,lons,lats =[],[],[]

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'] # In order to extract value from a nested dictionary, you put in the subkey after the main key
    lon= eq_dict['geometry']['coordinates'][0]
    lat= eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the earthquakes

data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat': lats,
    # marker attribute in the data is what displays the plots on the map and can be modified by different properties
    'marker':{
        'size':[5*mag for mag in mags],
        'color': mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'},
        }
    }]
my_layout = Layout(title='Global Earthquakes')

fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')


