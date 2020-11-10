from flask import (
    Flask, jsonify, request
)

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    myDict = { "name": 'pete', "stat": 'defence' }
    return jsonify(myDict)
