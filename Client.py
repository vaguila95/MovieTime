from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client.MovieTime
cinemas = db.cinemas

movies = list()
for c in cinemas.find({}, {'_id': 0}):
    for m in c['movies']:
        movies.append(m['name'].capitalize())

mid = 1
for m in movies:
    print(str(mid) + '. ' + m)
    mid += 1

movie_id = input(
    "Ingrese el id de la pelicula que desea ver\n\t> "
)

while not movie_id.isnumeric() or int(movie_id) not in range(1, len(movies)):
    movie_id = input(
        "Id inválido\nIngrese el id de la pelicula que desea ver\n\t> "
    )

# if __name__ == '__main__':
#     app.run()