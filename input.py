from pymongo import *
import datetime

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

db = client.testing_db # client.['testing_db']

collection = db.collection1 # db.['collection1']

post = {
    "title": "Doc One",
    "author": "Ichsan Kurnia",
    "text": "This is my first documents",
    "tags": ["Python", "MongoDB", "pymongo"],
    "date": datetime.datetime.now()
}

# posts = db.posts
post_id = db.collection1.insert(post)

print(post_id)