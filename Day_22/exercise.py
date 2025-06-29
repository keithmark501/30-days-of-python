import requests
from bs4 import BeautifulSoup
import json

def scrape_bu_stats(url, out_file):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    data = {}

    for p in soup.select('div#content p'):
        bold = p.find('strong')
        if bold and ':' in p.text:
            key, val = p.text.split(':', 1)
            data[key.strip()] = val.strip()

    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

scrape_bu_stats(
    'http://www.bu.edu/president/boston-university-facts-stats/', 
    'bu_stats.json'
)

import pandas as pd

def scrape_uci_datasets(url, out_file):
    dfs = pd.read_html(url)
    if not dfs:
        raise ValueError("No tables found")
    df = dfs[0]
    df.columns = df.columns.map(lambda c: c.strip())
    df.to_json(out_file, orient='records', indent=2)

scrape_uci_datasets(
    'https://archive.ics.uci.edu/ml/datasets.php', 
    'uci_datasets.json'
)

import requests
from bs4 import BeautifulSoup
import json

def scrape_presidents(url, out_file):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    presidents = []

    headers = [th.get_text(strip=True) for th in table.find_all('th')]
    rows = table.find_all('tr')[1:]

    for tr in rows:
        cells = tr.find_all(['td', 'th'])
        if len(cells) < 4:
            continue
        entry = {headers[i]: cells[i].get_text(strip=True) 
                 for i in range(min(len(cells), len(headers)))}
        presidents.append(entry)

    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(presidents, f, indent=2, ensure_ascii=False)

scrape_presidents(
    'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States',
    'us_presidents.json'
)