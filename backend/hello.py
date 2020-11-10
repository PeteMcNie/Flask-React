from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    myDict = { "name": 'pete', "stat": 'defence' }
    return myDict
