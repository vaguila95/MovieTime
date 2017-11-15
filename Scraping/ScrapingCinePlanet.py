import json

from Scraping import resources as r

url = 'https://portal.cineplanet.cl/#/'
cineplanet = dict()
cineplanet['name'] = 'cineplanet'
cineplanet['movies'] = list()

planet_soup = r.souping(url)
planet_str = str(planet_soup.findAll('script')[2].text)[11:-2]
planet_json = json.loads(planet_str)

for movie in planet_json['main']['billboard']:
    pelicula = dict()
    pelicula['name'] = movie['nomComercial']
    pelicula['cinemas'] = list()
    # print(pelicula['name'])

    # url_pelicula = url + '/pelicula/' + movie['codPelicula']
    # pelicula_soup = r.souping(url_pelicula)
    # pelicula_str = str(pelicula_soup.findAll('script')[2])[11:-2]
    # pelicula_json = json.loads(pelicula_str)

url_pelicula = url + '/pelicula/' + planet_json['main']['billboard'][0]['codPelicula']
print(r.selenium(url_pelicula).prettify())
# pelicula_soup = r.souping(url_pelicula)
# pelicula_str = str(pelicula_soup.findAll('script')[2])[11:-2]
# pelicula_json = json.loads(pelicula_str)
# print(pelicula_json)
