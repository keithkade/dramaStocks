from datetime import datetime
from flask import render_template
from FlaskWebProject import app, mongo

import nltk

@app.route('/')
def home():
    prices = list(mongo.db.prices.find({},{'ticker':1}))
    
    return render_template('index.html', prices=prices)
