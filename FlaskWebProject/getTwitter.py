import oauth2, json
from config import *
from pymongo import MongoClient

client = MongoClient('mongodb://40.78.151.253:27017/')

db = client.stocks
tweets = db.tweets

tweets.remove({})

"""
    data structure:
        tweets
        - company name
            - text
            - favorites
            - followers
            - retweets
            - date
"""

#twitter
def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers)
    return content

for stock in stocks:
    req = json.loads(oauth_req('https://api.twitter.com/1.1/search/tweets.json?q=\$%s'%(stock), ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET))
    stuff = []
    for post in req['statuses']:
        stuff.append({
            'text': post['text'],
            'favorites': post['favorite_count'],
            'retweet': post['retweet_count'],
            'followers': post['user']['followers_count'],
            'date': post['created_at'],
            'id': post['id'],
        })
    tweets.insert({'name': stock, 'tweets' : stuff})
