from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def souping(url):
    client = uReq(url)
    html = client.read()
    client.close()
    return soup(html, "html.parser")