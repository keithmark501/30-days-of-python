import requests
from collections import Counter
import re

romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(romeo_and_juliet)
text = response.text

words = re.findall(r'\b\w+\b', text.lower())
top_10_words = Counter(words).most_common(10)
print("Top 10 Most Frequent Words in Romeo and Juliet:")
print(top_10_words)
countries_api = 'https://restcountries.com/v3.1/all'
response = requests.get(countries_api)
countries_data = response.json()

largest_countries = sorted(countries_data, key=lambda x: x.get('area', 0), reverse=True)[:10]
print("Top 10 Largest Countries by Area:")
for country in largest_countries:
    print(f"{country['name']['common']}: {country.get('area', 0)} km²")

language_count = Counter()
all_languages = set()

for country in countries_data:
    langs = country.get('languages')
    if langs:
        for lang in langs.values():
            language_count[lang] += 1
            all_languages.add(lang)

print("\nTop 10 Most Spoken Languages:")
for lang, count in language_count.most_common(10):
    print(f"{lang}: spoken in {count} countries")

print(f"\nTotal number of unique languages: {len(all_languages)}")
from bs4 import BeautifulSoup

uci_url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(uci_url)
soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('table', {'border': '1'})
dataset_names = []

for table in tables:
    rows = table.find_all('tr')[1:]  
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 0:
            link = cols[0].find('a')
            if link:
                dataset_names.append(link.text.strip())

print(f"Found {len(dataset_names)} datasets:")
print(dataset_names[:20])  