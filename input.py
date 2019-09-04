from pymongo import *
import datetime
from pprint import *

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

db = client.testing_db # client.['testing_db']

# create collection
collection1 = db.collection1
# collection1 = db.['collection1']

post = {
    "title": "Doc One",
    "author": "Ichsan Kurnia",
    "text": "This is my first documents",
    "tags": ["Python", "MongoDB", "pymongo"],
    "date": datetime.datetime.now()
}

# insert doeccuments
post_id = db.collection1.insert(post)

show_doc = collection1.find_one()

# print(collection1.find_one())
pprint(show_doc)