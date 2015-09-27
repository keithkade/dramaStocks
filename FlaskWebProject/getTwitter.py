import oauth2

#twitter
def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

print oauth_req('https://api.twitter.com/1.1/search/tweets.json?q=lol', ACCESS_TOKEN_KEY, ACCESS_TOKEN_TOKEN)
