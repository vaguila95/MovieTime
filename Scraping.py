from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# películas CineMark
url = 'https://www.cinemark.cl/movies'
client = uReq(url)
html = client.read()
client.close()
mark_soup = soup(html, "html.parser")
peliculas = mark_soup.findAll('li', {'class': 'item movie-list-li box'})
for pelicula in peliculas:
    titulo = pelicula.div.h4.a.text
    print(titulo)
