from app import app
from flask import redirect, url_for
from flask_pymongo import PyMongo
import pandas as pd

app.config['MONGO_URI'] = 'mongodb://localhost:27017/aves'
mongo = PyMongo(app).db
print(mongo)
@app.route('/load')
def load_data():
    birds = mongo.birds
    data = birds.find()

