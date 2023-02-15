import redis
from flask import Flask, request, render_template, jsonify
#r = redis.Redis(host="0.0.0.0", port=6379,db=0)

app = Flask(__name__, template_folder="Templates") 
#r.set('nikunj',"Rabadiya")
@app.route("/")
def index():
    return 'hey'
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)