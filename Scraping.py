import json
from ScrapingCineMark import cinemark

collection = list()

with open('db.json', 'w') as file:
    json.dump(cinemark, file)