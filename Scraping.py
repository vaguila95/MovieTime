from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def souping(url):
    client = uReq(url)
    html = client.read()
    client.close()
    return soup(html, "html.parser")

ret = dict()


# CineMark
url = 'https://www.cinemark.cl/movies'
ret['cinemark'] = dict()

mark_soup = souping(url)
peliculas = mark_soup.findAll('li', {'class': 'item movie-list-li box'})
# cines = list()
# for o in souping(peliculas[0].div.a['href']).findAll('select', {
#         'class': 'movie-showtimes-selector'
#     })[0].findAll('option'):
#     if o['value'] != '':
#         cines.append(o['value'])
for pelicula_html in peliculas:
    cinemark_dic['name'] = pelicula_html.div.h4.a.text.lower()
    cines = dict()

    url_pelicula = pelicula_html.div.a['href']
    pelicula_soup = souping(url_pelicula)
    for option in pelicula_soup.findAll('select', {
        'class': 'movie-showtimes-selector'
    })[0].findAll('option'):
        cine_key = option['value']
        cine_value = dict()

        for ul in pelicula_soup.findAll('ul', {
            'class': 'movie-showtime-panel ' + cine_key
        }):
            salas_value = dict()

            for li in ul.findAll('li'):
                if li['class'] == 'showtime-detail':
                    pass
                else:
                    salas_key =

    # Opción 2
    # url = 'https://www.cinemark.cl/movies'
    # ret['empresa'] = dict()
    #
    # mark_soup = souping(url)
    # peliculas = mark_soup.findAll('li', {'class': 'item movie-list-li box'})
    # # cines = list()
    # # for o in souping(peliculas[0].div.a['href']).findAll('select', {
    # #         'class': 'movie-showtimes-selector'
    # #     })[0].findAll('option'):
    # #     if o['value'] != '':
    # #         cines.append(o['value'])
    # for pelicula_html in peliculas:
    #     cinemark_dic['name'] = pelicula_html.div.h4.a.text.lower()
    #     cines = dict()
    #
    #     url_pelicula = pelicula_html.div.a['href']
    #     pelicula_soup = souping(url_pelicula)
    #     for option in pelicula_soup.findAll('select', {
    #         'class': 'movie-showtimes-selector'
    #     })[0].findAll('option'):
    #         cine_key = option['value']
    #         cine_value = dict()
    #
    #         for ul in pelicula_soup.findAll('ul', {
    #             'class': 'movie-showtime-panel ' + cine_key
    #         }):
    #             salas_value = dict()
    #
    #             for li in ul.findAll('li'):
    #                 if li['class'] == 'showtime-detail':
    #                     pass
    #                 else:
    #                     salas_key =
