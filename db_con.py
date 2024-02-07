from bson import ObjectId
from flask_pymongo import PyMongo
import pandas as pd


class DBCon():

    def __init__(self, app):
        self.__app = app
        self.__app.config['MONGO_URI'] = 'mongodb://localhost:27017/aves'
        self.__mongo = PyMongo(app)
        self.__birds = self.__mongo.db.birds
        self.__users = self.__mongo.db.users

    def get_birds(self):
        return self.__birds

    def get_users(self):
        return self.__users

    def get_unique_data(self, db, col):
        return list(db.distinct(col))

    def load_data(self, db, condition=None):
        data = pd.DataFrame(list(db.find(condition)))
        return data

    def get_bird_cols(self, condition, cols_query):

        return pd.DataFrame(list(self.__birds.find(condition, cols_query)))

    def search_user(self, gmail, password):
        return self.__users.find_one({'user_gmail': gmail, 'user_pass': password})

    def search_bird(self, condition):
        return self.__birds.find_one(condition)

    def insert_user_find(self, user, bird_oid):
        user_oid = user.iloc[0]['_id']
        self.__users.update_one({'_id': user_oid}, {'$push': {'user_find': {'bird_id': bird_oid, 'fav': False}}})

    def change_user_find_fav(self, user, bird_oid, fav=True):
        user = user.iloc[0]['_id']
        self.__users.update_one({'_id': user, 'user_find.bird_id': bird_oid}, {'$set': {'user_find.$.fav': fav}})

    def delete_user_find(self, user, bird_oid):
        user_oid = user.iloc[0]['_id']
        self.__users.update_one({'_id': user_oid}, {'$pull': {'user_find': {"bird_id": bird_oid}}})

    def test(self):
        print(list(self.__birds.find(
            {'$and': [{'bird_color.color_name': {'$in': ['Black']}}, {'bird_habitat': {'$in': ['Ocean']}}, {'bird_scale': 6}, {'bird_order': 'Procellariiformes'}]},
            {'_id': 1, 'bird_name': 1, 'bird_sci_name': 1, 'bird_color': 1, 'bird_img' : 1})
))



if __name__ == '__main__':
    from app import app

    db_con = DBCon(app)
    """birds = db_con.get_bird_cols({"_id" : 1, "bird_name" : 1})
    for habitat in db_con.get_unique_data(db_con.get_birds(), "bird_habitat"):
        print(f"(\"{habitat},\" .jpg)")
    print()
    print()
    for habitat in db_con.get_unique_data(db_con.get_birds(), "bird_order"):
        print(f"(\"{habitat}\", \"{habitat}.jpg\"),")

    scale = db_con.get_unique_data(db_con.get_birds(),'bird_scale')
    print(scale)

    print()
"""
    db_con.test()
    # birds = db_con.get_birds()
    # print(birds)
    # bird_id = birds.iloc[0]['_id']
    # bird = db_con.search_bird(birds.iloc[0]['_id'])
    # print(bird_id)

    # print(db_con.search_bird("65b767bd0418ddceb0fcb308"))

"""
{bird_color: {$elemMatch: { $elemMatch: { $eq: 'Green' }}}}


def load_data(db, condition=None):
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


birds_data = load_data(birds)
print(birds_data)
# delete_user_find(user, bird_id)
# insert_user_find(user, bird_id)
# change_user_find_fav(user_id, bird_id, fav=False)


{'$and': [{
      "bird_color.color_name": {
        "$all": ["Black", "Red"]
      }
    },
    {
      "bird_scale": 2
    }
  ]
}
"""
