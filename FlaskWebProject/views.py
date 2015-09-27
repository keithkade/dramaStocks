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


    #begin stupid stop picking

    bought = False
    highRetweet = 0
    buyDate = ''
    sellDate = ''
    for thing in  prices[0]['tweets']:
        reCount =  thing['retweet']
        dateStr = parse(thing['date']).strftime('%Y-%m-%d')
        if highRetweet < reCount:
            highRetweet = reCount

        if reCount > 0 and not bought and buyDate == '':
            bought = True
            buyDate = dateStr

        if reCount < highRetweet and bought and dateStr > buyDate and sellDate == '':
            bought = False
            sellDate = dateStr

    print Trader.buySell('IBM', buyDate, sellDate, 1000)
    print Trader.buySell('DJI', buyDate, sellDate, 1000)

    return render_template('index.html', prices=prices)
