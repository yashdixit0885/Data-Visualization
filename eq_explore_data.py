
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data

filename = 'Data Visualization/data/oneday.json'
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)
    

readable_file = 'Data Visualization/data/readable_eq_data.json'

with open(readable_file, 'w') as f:
    json.dump(all_eq_data,f,indent=4)

all_eq_dicts = all_eq_data['features']

all_eq_title = all_eq_data['metadata']['title']

mags,lons,lats,hover_texts =[],[],[],[]

for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes

data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    # marker attribute in the data is what displays the plots on the map and can be modified by different properties
    'marker':{
        'size':[5*mag for mag in mags],
        'color': mags,
        'colorscale':'YlOrRd',
        'reversescale':False,
        'colorbar':{'title':'Magnitude'},
        }
    }]
my_layout = Layout(title=all_eq_title)

fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')


