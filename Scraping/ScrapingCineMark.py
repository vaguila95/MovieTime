import resources as r

url = 'https://www.cinemark.cl/movies'
cinemark = dict()
cinemark['name'] = 'cinemark'
cinemark['movies'] = list()
mark_soup = r.souping(url)
peliculas = mark_soup.findAll('li', {'class': 'item movie-list-li box'})

for pelicula_html in peliculas:
    pelicula = dict()
    pelicula['name'] = pelicula_html.div.h4.a.text.lower()
    pelicula['theaters'] = list()

    url_pelicula = pelicula_html.div.a['href']
    pelicula_soup = r.souping(url_pelicula)
    for option in pelicula_soup.findAll(
            'select', {'class': 'movie-showtimes-selector'}
    )[0].findAll('option')[1:]:
        cine = dict()
        cine['name'] = option['value']
        cine['rooms'] = list()

        # cada ul es un cine distinto
        cine_html = pelicula_soup.findAll('ul', {
            'class': 'movie-showtime-panel ' + cine['name']
        })[0].findAll('li')

        for li in cine_html:

            if li.h3 is not None:
                sala = dict()
                sala['name'] = li.h3.text
                sala['days'] = list()
                cine['rooms'].append(sala)

            elif li.ul is not None:
                for d in li.ul.findAll('li'):
                    dia = dict()
                    dia['day'] = d.find('span', {'class': 'showtime-day'}).text
                    dia['schedule'] = list()
                    for h in d.findAll('span', {'class': 'showtime-hour'}):
                        dia['schedule'].append(h.text)
                    cine['rooms'][-1]['days'].append(dia)
        pelicula['theaters'].append(cine)
    cinemark['movies'].append(pelicula)
