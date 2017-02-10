from app import app
import redis,json
from flask import jsonify,render_template

db = redis.Redis('localhost',port='6379')

@app.route('/')
@app.route('/index')
def index():
  return "Hello, World!"
@app.route('/api/<date>')
def get_data(date):
    response = db.get(date)
    graphlist=response.replace('[','').replace(']','').replace(', {','').replace('{','').replace(', \'\'','').replace('\"','\'').encode('utf-8').split('}')
    response_list = []
    max_cluster=0
    for subreddit in graphlist:
        if subreddit:
            split1=subreddit.split(', \'subreddit\': ')
            subname=split1[1]
            split2=split1[0].split(', \'clusterdist\': ')
            cdist = float(split2[1])
            split3=split2[0].split(', \'subsize\': ')
            subsize=int(split3[1])
            clusternum=split3[0].split('\'cluster\': ')[1]
            if int(clusternum) > max_cluster:
                max_cluster = int(clusternum)
            max_cluster = max_cluster+1
            if subsize > 100:
                response_list.append({'id':subname,'clusternum':clusternum,'cdist':cdist,'subsize':subsize})
    return render_template('index.html',cluster=response_list, numclusters=max_cluster)
