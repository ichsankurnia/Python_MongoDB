from pymongo import *
import datetime
from pprint import *

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

db = client.testing_db

new_posts = [
	{
	    "title": "Doc Two",
	    "author": "Mutia Shafira",
	    "text": "A text of second documents",
	    "tags": ["C#", "Python", "Tensorflow"],
	    "date": datetime.datetime.now()
	},
	{
		"title": "Doc Three",
	    "author": "Irfan Kurnia",
	    "text": "Text of third documents",
	    "tags": ["MM", "TK", "Game"],
	    "date": datetime.datetime.now()
	}
]

# create collection
collection1 = db.collection1

collection1.insert_many(new_posts)
collection1.insert(new_posts)

# show_doc = collection1.find_one()

for post in collection1.find():
	pprint(post)

