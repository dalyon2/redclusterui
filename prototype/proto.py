from flask import Flask,render_template
import redis

db = redis.Redis('localhost',port='6379')
app=Flask(__name__)

@app.route('/')
def coolstuff():
    return render_template('index.html')    
@app.route('/<path:path>', methods = ['PUT', 'GET'])
def home(path):
    if not db.exists(path): #does the hash exist?
        return "Error: thing doesn't exist"
    event = db.get(path)
    return event
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)

