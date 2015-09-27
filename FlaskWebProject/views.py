from datetime import datetime
from flask import render_template
from FlaskWebProject import app

@app.route('/')
def home():
    return render_template('index.html')
