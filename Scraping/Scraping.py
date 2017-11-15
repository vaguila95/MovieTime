import json
from ScrapingCineMark import cinemark
from pymongo import MongoClient

client = MongoClient()
db = client.MovieTime
cinemas = db.cinemas
cinemas_collection = list()

cinemas.insert_one(cinemark)
cinemas_collection.append(cinemark)

with open('cinemas.json', 'w') as file:
    json.dump(cinemas_collection, file)
