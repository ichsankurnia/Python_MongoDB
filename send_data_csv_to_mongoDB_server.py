import csv
from math import gamma, exp
import pandas as pd
import plotly.graph_objects as graph

from pymongo import *
import datetime
from pprint import *

# client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')
client = MongoClient("mongodb+srv://ichsankurnia:ichsan14@testcluster1-hi7ql.mongodb.net/test?retryWrites=true&w=majority")

db = client.db_dataAngin

db = client.test_db

df = pd.read_csv('../bbta3/DataAngin/anm3.2_BRIDGE_SISI PASURUAN.csv', sep=';')

df = df[(df.X > 0 ) & (df.X < 2)]

df.sort_values('X', inplace=True) # tim data yg lama jika ada data yg baru

list_Time 	= df.Time.tolist()
list_X 		= df.X.tolist()
list_Y	 	= df.Y.tolist()
list_Z 		= df.Z.tolist()

list_dataAngin = []
data_angin = {}

for i in range(len(list_Time)):
	data_angin = {
		"time" : list_Time[i],
		"X" : list_X[i],
		"Y" : list_Y[i],
		"Z" : list_Z[i],
	}
	list_dataAngin.append(data_angin)

print(list_dataAngin)

for doc in list_dataAngin:
	db.DataAngin.insert(doc)

for i in db.data.find():
	pprint(i)