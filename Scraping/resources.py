from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from contextlib import closing
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait


def souping(url):
    client = uReq(url)
    html = client.read()
    client.close()
    return soup(html, "html.parser")


def selenium(url):
    with closing(Firefox()) as browser:
        browser.get(url)
        button = browser.find_element_by_name('button')
        button.click()
        # wait for the page to load
        WebDriverWait(browser, timeout=10).until(
            lambda x: x.find_element_by_id('someId_that_must_be_on_new_page'))
        # store it to string variable
        page_source = browser.page_source
    return soup(page_source, 'html.parser')
