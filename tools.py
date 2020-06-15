"""
This package will contain the tools, used by coderpaddy
To aid in scraping websites.
"""

# Dependecies
import requests
from bs4 import BeautifulSoup as BS


def get_soup(url):
    r = requests.get(url)
    soup = BS(r.content, 'html.parser')
    return soup

def get_elem(*args):
    soup, tag_type, id_type, search_term = args
    elem = soup.find(tag_type, {f"{id_type}": search_term})
    return elem

def get_elems(*args):
    soup, tag_type, id_type, search_term = args
    elems = soup.find_all(tag_type, {f"{id_type}": search_term})
    return elems


if __name__ == "__main__":
    print("This is aimed to be a helper file. not to be used individucally")