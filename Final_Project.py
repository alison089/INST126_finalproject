# This Python Program will allow users to learn more about Comedian Bobby Lee in all of his achievements. 
# His Wikipedia page has become scrapped via this program to provide you quick overview of his Wiki page
# Additionally, I decided to use pandas and numpy arrays to catorigze Bobby Lee's film apperances. 

import os
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


url = 'https://en.wikipedia.org/wiki/Bobby_Lee'
lee_page = requests.get(url)
 # print(lee_page.text) , to look at the html

lee_soup = BeautifulSoup(lee_page.content, "html.parser")
type(lee_soup)

# scraping the table of their mini headers
lee_table = lee_soup.find("table")
print(lee_table)
lee_th = lee_soup.find_all("th")
print(lee_th)
lee_header = []
for th in lee_th:
    lee_header.append(th.get_text().strip())
header_string = ",".join(lee_header)
print(lee_header)

# scraping the content in the table adjacent to the mini headers. This indicates the responses to the catagories in the table haders.
table_rows = lee_table.find_all("tr")
table_rows
lee_rows = [header_string]
for row in table_rows:
    row_list = []
    print(row)
    for cell in row.find_all("td"):
        cell_text = cell.get_text().strip()
        row_list.append(cell_text)
    row_string = ",".join(row_list)
    lee_rows.append(row_string)
lee_rows

# I utilized pandas in order to write data on Bobby Lee's acting history then changing it to a CSV.
filmography = [{'Year': '1999', 'Title' : 'The Underground Comedy Movie', 'Role': 'Chinese Man'},
                {'Year': '2003', 'Title' : 'Pauly Shore is Dead', 'Role': 'Delivery Boy'}, 
                {'Year': '2004', 'Title' : 'Harold & Kumar Go to White Castle', 'Role': 'Kenneth Park'},
                {'Year': '2005', 'Title' : 'Accidentally on Purpose', 'Role': 'Bobby'},
                {'Year': '2006', 'Title' : 'Undoing', 'Role': 'Kenny'},
                {'Year': '2007', 'Title' : 'Kickin It Old Skool', 'Role': 'Aki'},
                {'Year': '2008', 'Title' : 'Pineapple Express', 'Role': 'Bobby'},
                {'Year': '2009', 'Title' : 'Soldiers of Capernaum', 'Role': 'Bobby'},
                {'Year': '2010', 'Title' : 'Hard Breakers', 'Role': 'Travis'},
                {'Year': '2011', 'Title' : 'Paul', 'Role': 'Valet'},
                {'Year': '2012', 'Title' : 'The Dictator', 'Role': 'Mr.Lao'},
                {'Year': '2013', 'Title' : 'Final Recipe', 'Role': 'Park'},
                {'Year': '2014', 'Title' : 'Meet Me at the Reck', 'Role': 'Bobby Lee'},
                {'Year': '2015', 'Title' : 'The Comments', 'Role': 'Hugh'},
                {'Year': '2016', 'Title' : 'Laid in America', 'Role': 'Goose'},
                {'Year': '2018', 'Title' : 'Curious Georgina', 'Role': 'Bobby'},
                {'Year': '2019', 'Title' : 'Extracurricular Activities', 'Role': 'Mr.Mulnick'},
                {'Year': '2020', 'Title' : 'The Wrong Missy', 'Role': 'Check-In Desk Employee'},
                {'Year': '2021', 'Title' : 'Wish Dragon', 'Role': 'Tall Goon'},
                {'Year': '2023', 'Title' : 'Death and Ramen', 'Role': 'Timmy Lee'}]

df = pd.DataFrame(filmography)
df = df[['Year', 'Title', 'Role']]
df.head
df.to_csv('filmography.csv', index = False, header = True)

np.arange(len("filmography"))
np.arange(len("The Underground Comedy Movie"))








