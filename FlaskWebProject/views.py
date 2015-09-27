from datetime import datetime
from flask import render_template
from FlaskWebProject import app, mongo
from textblob import TextBlob

import nltk

@app.route('/')
def home():
    #prices = list(mongo.db.prices.find({},{'ticker':1}))
    prices = list(mongo.db.tweets.find({}))

    return render_template('index.html', prices=prices)
