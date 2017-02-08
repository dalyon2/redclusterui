from flask import Flask,render_template
import redis,json

db = redis.Redis('localhost',port='6379')
app=Flask(__name__)

@app.route('/')
#def coolstuff():
#    return render_template('index.html')    
@app.route('/<path:path>', methods = ['PUT', 'GET'])
def home(path):
    if not db.exists(path): #does the hash exist?
        return "Error: thing doesn't exist"
    event = db.get(path)
    graphlist=event.replace('[','').replace(']','').replace(', {','').replace('{','').replace(', \'\'','').replace('\"','\'').encode('utf-8').split('}')
    fakelist=[]
    for subreddit in graphlist:
        if subreddit:
            split1=subreddit.split(', \'subreddit\': ')
            subname=split1[1]
            split2=split1[0].split(', \'clusterdist\': ')
            cdist = float(split2[1])
            split3=split2[0].split(', \'subsize\': ')
            subsize=int(split3[1])
            clusternum=split3[0].split('\'cluster\': ')[1]
            fakelist.append({'id':subname,'clusternum':clusternum,'cdist':cdist,'subsize':subsize})
    return render_template('table.html',stuff=fakelist)
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
