from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    total = str(eggs())
    return total


def eggs():
    number = 6
    boxes = 56
    return number * boxes