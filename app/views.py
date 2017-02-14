from app import app
import redis,json
from flask import jsonify,render_template,request

db = redis.Redis('localhost',port='6379',password='')

@app.route('/')
@app.route('/index')
def index():
  return render_template('default.html')

@app.route('/', methods=['POST'])
def get_post_data():
    year=request.form["year"]
    month=request.form["month"]
    response = db.get(str(year)+"-"+str(month))
    graphlist=response.replace('[','').replace(']','').replace('{','').replace('\"','').encode('utf-8').split('}')
    response_list = []
    max_cluster=0
    for subreddit in graphlist:
        if subreddit:
            split1=subreddit.split(', \'subreddit\': ')
            subname=split1[1].replace('u\'','').replace('\'','')
            split2=split1[0].split(', \'subsize\': ')
            subsize=int(split2[1])
            clusternum=int(split2[0].split('\'cluster\': ')[1])
            if (subsize > 600):
                response_list.append({'subreddit':subname,'cluster':clusternum,'subsize':subsize})
            if clusternum > max_cluster:
                max_cluster = clusternum
    max_cluster = max_cluster+1
    return render_template('index.html',cluster=response_list, numclusters=max_cluster, graphyear=year, graphmonth=month)
    

@app.route('/api/<date>')
def get_data(date):
    response = db.get(date)
    graphlist=response.replace('[','').replace(']','').replace('{','').replace('\"','').encode('utf-8').split('}')
    response_list = []
    max_cluster=0
    for subreddit in graphlist:
        if subreddit:
            split1=subreddit.split(', \'subreddit\': ')
            subname=split1[1].replace('u\'','').replace('\'','')
            split2=split1[0].split(', \'subsize\': ')
            subsize=int(split2[1])
            clusternum=int(split2[0].split('\'cluster\': ')[1])
            response_list.append({'subreddit':subname,'cluster':clusternum,'subsize':subsize})
            if clusternum > max_cluster:
                max_cluster = clusternum
    max_cluster = max_cluster+1
    return render_template('index.html',cluster=response_list, numclusters=max_cluster)
