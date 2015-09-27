from datetime import datetime
from flask import render_template
from FlaskWebProject import app, mongo
#from trader import Trader
from textblob import TextBlob


import nltk

@app.route('/')
def home():
    #prices = list(mongo.db.prices.find({},{'ticker':1}))
    prices = list(mongo.db.tweets.find({'name':'IBM'}))
    for thing in  prices[0]['tweets']:
        print thing['retweet']
        print thing['date']


    return render_template('index.html', prices=prices)
