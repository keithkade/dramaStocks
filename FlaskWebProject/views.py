from datetime import datetime
from flask import render_template
from FlaskWebProject import app, mongo, request
from trader import Trader
from textblob import TextBlob
from dateutil.parser import parse

import nltk

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        names = list(mongo.db.prices500.find({'ticker':request.form['name'].upper()}))
        tweets = list(mongo.db.tweets500.find({'name':request.form['name'].upper()}))
        dow = list(mongo.db.prices500.find({'ticker':"DJI"}))
        result = Trader.buySell(request.form['name'].upper(),"2015-09-21","2015-09-25",1000)

        return render_template('index.html',name=request.form['name'].upper(), names= round(int(result),2), prices=names[0]['prices'][:10], dow=dow[0]['prices'][:10])
    else:

    #stocks = ['AAPL', 'IBM', 'MMM', 'MSFT', 'ATVI']




    #prices = list(mongo.db.prices.find({},{'ticker':1}))


    #34463bad7e819fc5d858f0af40d3c69e
    #begin stupid stock picking
    #
    # bought = False
    # highRetweet = 0
    # buyDate = ''
    # sellDate = ''
    # for thing in  prices[0]['tweets']:
    #     reCount =  thing['retweet']
    #     dateStr = parse(thing['date']).strftime('%Y-%m-%d')
    #     if highRetweet < reCount:
    #         highRetweet = reCount
    #
    #     if reCount > 0 and not bought and buyDate == '':
    #         bought = True
    #         buyDate = dateStr
    #
    #     if reCount < highRetweet and bought and dateStr > buyDate and sellDate == '':
    #         bought = False
    #         sellDate = dateStr
    #
    # print buyDate
    # print sellDate
    # print Trader.buySell(ticker, buyDate, sellDate, 1000)
    #
    #
    # print Trader.buySell('DJI', buyDate, sellDate, 1000)

        return render_template('index.html')
