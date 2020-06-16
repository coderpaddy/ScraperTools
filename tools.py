"""
This package will contain the tools, used by coderpaddy
To aid in scraping websites.
"""

# Dependecies
import requests
import csv
from datetime import date
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

def convert_date_ws_ns(_date):
    """
    Convert date from 'Jun 25th' to 25/06/YY
    """
    month_dict = {
        "jan": "01",
        "feb": "02",
        "mar": "03",
        "apr": "04",
        "may": "05",
        "jun": "06",
        "jul": "07",
        "aug": "08",
        "sep": "09",
        "oct": "10",
        "nov": "11",
        "dec": "12"
    }
    month_word, day_num = _date.split(" ")
    if len(day_num) == 4:
        day_num = day_num[:2]
    else:
        day_num = f"0{day_num[:1]}"
    month_num = month_dict[month_word.lower()]
    return f"{day_num}/{month_num}/{date.today().strftime('%Y')}"

if __name__ == "__main__":
    print("This is aimed to be a helper file. not to be used individucally")
