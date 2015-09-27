from datetime import datetime
from flask import render_template
from FlaskWebProject import app, mongo
from trader import Trader
from textblob import TextBlob
from dateutil.parser import parse

import nltk

@app.route('/')
def home():
    #prices = list(mongo.db.prices.find({},{'ticker':1}))
    prices = list(mongo.db.tweets.find({'name':'IBM'}))


    baught = False
    buyDate = ''
    sellDate = ''
    for thing in  prices[0]['tweets']:
        reCount =  thing['retweet']
        dateStr = parse(thing['date']).strftime('%Y-%m-%d')
        if reCount > 0:
            baught = True
            buyDate = dateStr
        if reCount == 0 and baught:
            baught = False
            sellDate = dateStr

    print buyDate
    print sellDate
    print Trader.buySell('IBM', buyDate, sellDate, 1000)

    return render_template('index.html', prices=prices)
