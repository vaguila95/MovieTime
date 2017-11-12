import json
from ScrapingCineMark import cinemark

collection = list()
collection.append(cinemark)

with open('db.json', 'w') as file:
    json.dump(collection, file)
