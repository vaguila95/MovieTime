from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.cinemark.cl/movies/asesinato-en-el-expreso-de-oriente'
client = uReq(url)
html = client.read()
client.close()
pelicula_soup = soup(html, "html.parser")
a = pelicula_soup.find('ul', {
            'class': 'movie-showtime-panel alto-las-condes'}).findAll('li')

print(*a[0].h3, sep='\n')

