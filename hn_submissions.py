from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline

import requests

#Make an API call and store the response

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code:{r.status_code}")

# Process information about each submission

submission_ids = r.json()


submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r= requests.get(url)
    print(f"id:{submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()
    

    #Build a dictionary for each title
    submission_dict = {
        'owner':response_dict['by'],
        'hn_link':f"http://news.ycombinator.com/item?id={submission_id}",
        'score':response_dict['score'],
        }
    submission_dicts.append(submission_dict)
    submission_dicts = sorted(submission_dicts,key=itemgetter('score'),reverse=True)

scores,owners = [],[]

for submission_dict in submission_dicts:
    scores.append(submission_dict['score'])
    owners.append(submission_dict['owner'])

#Make Visualization

data = [{
    'type':'bar',
    'x':owners,
    'y':scores,
    'marker':{
        'color':'rgb(60,100,150)',
        'line':{'width':1.5,'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,
}]

my_layout = {
    'title':'Most scored owners on Hacker News',
    'titlefont':{'size':28},
    'xaxis':{
        'title':'Articles',
        'titlefont':{'size':24},
        'tickfont':{'size':14}
        },
    'yaxis':{
        'title':'Scores',
        'titlefont':{'size':24},
        'tickfont':{'size':14}
    }
    }

fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='hn_scores.html')