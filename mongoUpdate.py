from pymongo import MongoClient

client = MongoClient('mongodb://40.78.151.253:27017/')

db = client.stocks
collection = db.tickers
collection2 = db.prices

import requests, json

def buySell(ticker, start, end, amt):
    data = collection2.find_one({'ticker' : ticker})
    if data:
        startPrice = 1
        endPrice = 1
        for price in data['prices']:
            if price['date'] == start:
                startPrice = price['open']
            elif price['date'] == end:
                endPrice = price['open']
        print startPrice
        print endPrice
        delta = (endPrice - startPrice) / startPrice
        return delta * amt


"""
stocks = [{'ticker': 'AAPL'},{'ticker': 'MMM'},{'ticker': 'MSFT'},{'ticker': 'IBM'},{'ticker': 'ATVI'}]
#for post in collection.find():
for post in stocks:
    entry = []
    ticker = post['ticker']
    if not collection2.find_one({'ticker' : ticker}):
        responseTxt = requests.get("https://www.quandl.com/api/v3/datasets/WIKI/" + ticker +  ".json?auth_token=1R-Q-a7d5EAN_TLsSQtx")
        try:
            response = json.loads(responseTxt.text)
            if ('dataset' in response):
                for thing in response['dataset']['data']:
                    entry.append({'date' : thing[0], 'open': thing[8]})
                collection2.insert({'ticker': ticker, 'prices': entry})
                print 'added ' + ticker
            else:
                print 'no data for ' + ticker
        except:
            print ticker + ' broke'
    else:
        print ticker + ' was in db'
"""

"""
col = collection2.find()
for post in col:
    print post['ticker']
"""

print buySell('MSFT', '1999-01-04', '2001-01-02', 1000)

print 'done'