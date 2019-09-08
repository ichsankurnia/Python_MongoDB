from pymongo import *
import datetime
from pprint import *

from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/')

db = client.testing_db

all_docs = db.collection1.find()

for doc in all_docs:
	pprint(doc)

print("\n==============")

pprint(db.collection1.find_one({"author": "Ichsan Kurnia"}))

print("\n================")

for post in db.collection1.find({"author": "Mutia Shafira"}):
	pprint(post)

print("\n===============")
pprint(db.collcetion1.count_documents({}))

print("\n===============")
pprint(db.collection1.count_documents({'author': 'Ichsan Kurnia'}))

print(datetime.datetime.now())