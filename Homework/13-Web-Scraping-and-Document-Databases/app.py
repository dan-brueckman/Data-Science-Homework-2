
# coding: utf-8

# In[10]:


from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
from bs4 import BeautifulSoup as bs
import requests as req
from splinter import Browser
import pandas as pd
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)

@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)


@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    data = scrape_mars.scrape()
    mars.update(
        {},
        data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

