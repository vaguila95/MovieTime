from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def souping(url):
    client = uReq(url)
    html = client.read()
    client.close()
    return soup(html, "html.parser")

collection = list()


# CineMark
url = 'https://www.cinemark.cl/movies'
cinemark = dict()
cinemark['name'] = 'cinemark'
cinemark['movies'] = list()
mark_soup = souping(url)
peliculas = mark_soup.findAll('li', {'class': 'item movie-list-li box'})

for pelicula_html in peliculas:
    pelicula = dict()
    pelicula['name'] = pelicula_html.div.h4.a.text.lower()
    print(pelicula['name'])
    pelicula['theaters'] = list()

    url_pelicula = pelicula_html.div.a['href']
    pelicula_soup = souping(url_pelicula)
    for option in pelicula_soup.findAll('select', {
        'class': 'movie-showtimes-selector'
    })[0].findAll('option'):
        cine = dict()
        cine['name'] = option['value']
        cine['rooms'] = list()
        print(pelicula_soup.findAll('ul', {
            'class': 'movie-showtime-panel ' + cine['name']
        }))

    #     for li in pelicula_soup.findAll('ul', {
    #         'class': 'movie-showtime-panel ' + cine['name']
    #     })[0].findAll('li'):
    #         if li['class'] != 'showtime-detail':
    #             sala = dict()
    #             sala['name'] = li.text.strip(':')
    #             sala['days'] = list()
    #             print(sala['name'])
    #         else:
    #             dia = dict()
    #             dia['day'] = li.findAll(
    #                 'span', {'class': 'showtime-day'}
    #             )[0].text
    #             dia['schedule'] = list()
    #             for span in li.findAll('span', {'class': 'showtime-hour'}):
    #                 dia['schedule'].append(span.text)
    #             cine['rooms'].append(sala)
    #     pelicula['theaters'].append(cine)
    # cinemark['movies'].append(pelicula)

collection.append(cinemark)
