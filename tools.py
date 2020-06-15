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

def write_csv(csv_doc, data_dict):
    fieldnames = [x.lower() for x in data_dict[1].keys()]
    writer = csv.DictWriter(csv_doc, fieldnames=fieldnames)
    writer.writeheader()

    for key in data_dict.keys():
        writer.writerow(data_dict[key])


if __name__ == "__main__":
    print("This is aimed to be a helper file. not to be used individucally")
