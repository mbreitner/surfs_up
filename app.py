#import flask dependency
from flask import Flask

#create a new flask instance
app = Flask(__name__)

#create the first flask route
@app.route('/')

#creat a hello_world function
def hello_world():
    return('Hello world!')