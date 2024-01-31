from bson import ObjectId
from flask import Flask
from app import app
from flask_pymongo import PyMongo
import pandas as pd

app.config['MONGO_URI'] = 'mongodb://localhost:27017/aves'
mongo = PyMongo(app)


birds = mongo.db.birds
users = mongo.db.users


def load_data(db, condition):
    data = pd.DataFrame(list(db.find(condition)))
    return data


def insert_user_find(user, bird_oid):
    user_oid = user.iloc[0]['_id']
    users.update_one({'_id': user_oid}, {'$push': {'user_find': {'bird_id': bird_oid, 'fav': False}}})


def get_unique_data(db, col):
    return list(db.distinct(col))


def change_user_find_fav(user_oid, bird_oid, fav=True):
    users.update_one({'_id': user_oid, 'user_find.bird_id': bird_oid}, {'$set': {'user_find.$.fav': fav}})


def delete_user_find(user, bird_oid):
    user_oid = user.iloc[0]['_id']
    users.update_one({'_id': user_oid}, {'$pull': {'user_find': {"bird_id": bird_oid}}})


bird = load_data(birds, {'bird_color': {'$all': ['#FF0000', '#FFFFFF', '#000000']}})
if not bird.empty:
    bird_id = bird.iloc[0]['_id']

user = load_data(users, {'user_name': 'Tone P'})
user_id = user.iloc[0]['_id']

user_name = load_data(users, {'_id': user_id}).iloc[0]['user_name']
print(user_name)
uni_color = get_unique_data(birds, 'bird_color')
print(uni_color)

# delete_user_find(user, bird_id)
# insert_user_find(user, bird_id)
# change_user_find_fav(user_id, bird_id, fav=False)
