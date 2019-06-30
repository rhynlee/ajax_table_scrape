#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import pandas as pd
import cssselect
import json

# Pull all table data using variables found from console

table_data = {
    'table_id': 'ptp_4f163d8a745148a7_1',
    'start' : 0,
    'length' : 500,
    'action': 'ptp_load_posts',
    '_ajax_nonce': '274d4075d5'
        }

result = requests.post('http://blas.com/wp-admin/admin-ajax.php', data=table_data)

df = pd.read_json(result.text)
links = []

for i in range(500):
    links.append(df.data[i]['title'])

raw_links = pd.DataFrame(links)
raw_links.to_json("./links.json")

with open('./links.json', 'r') as f:
        datastore = json.load(f)

clean_links = []
for i in range (500):
    soup = BeautifulSoup(datastore['0'][str(i)])
    for link in soup.find_all('a', href=True):
        clean_links.append(link['href'])

with open('clean_links.txt', 'w') as outfile:  
    json.dump(clean_links, outfile)