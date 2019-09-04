import csv
from math import gamma, exp
import pandas as pd
import plotly.graph_objects as graph

from pymongo import *
import datetime
from pprint import *

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

db = client.testing_db

df = pd.read_csv('../bbta3/DataAngin/anm3.2_BRIDGE_SISI PASURUAN.csv', sep=';')

df = df[(df.X > 1.5 ) & (df.X < 1.7)]

df.sort_values('X', inplace=True) # tim data yg lama jika ada data yg baru

data = df.iloc[0:5]

print(data)

# print(data.Y)
# data['X'] = df['X']
list_Time = data.Time.tolist()
list_X = data.X.tolist()
list_Y = data.Y.tolist()
list_Z = data.Z.tolist()

data_angin ={
	"time" : list_Time,
	"X": list_X,
	"Y": list_Z,
	"Z": list_Z,
}

db.DataAngin.insert(data_angin)

pprint(db.DataAngin.find_one())

# print("X: ", list_X)
# print("Y: ", list_Y)
# print("Z: ", list_Z)
# print(data)