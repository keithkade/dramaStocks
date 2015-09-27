from flask import Flask, request
from flask.ext.pymongo import PyMongo


app = Flask(__name__)

#config
app.config['MONGO_HOST'] = "40.78.151.253"
app.config['MONGO_DBNAME'] = "stocks"
mongo = PyMongo(app)


import FlaskWebProject.views
