from pymongo import *
import datetime
from pprint import *

client = MongoClient('mongodb://localhost:27017/')

db = client.testing_db

all_docs = db.collection1.find()

for doc in all_docs:
	pprint(doc)