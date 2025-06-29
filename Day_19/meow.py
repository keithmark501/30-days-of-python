import os
import json
import re
from collections import Counter
from typing import List, Tuple
import csv

def count_lines_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        word_count = sum(len(line.split()) for line in lines)
        return len(lines), word_count

def most_spoken_languages(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    language_counter = Counter()
    for country in data:
        for lang in country.get('languages', []):
            language_counter[lang] += 1
    return language_counter.most_common(n)

def most_populated_countries(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    countries_population = [{'country': country['name'], 'population': country['population']} for country in data]
    countries_population.sort(key=lambda x: x['population'], reverse=True)
    return countries_population[:n]

def extract_emails(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    emails = re.findall(r'\S+@\S+', content)
    return emails

def find_most_common_words(text_or_file, n):
    if os.path.isfile(text_or_file):
        with open(text_or_file, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = text_or_file
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(n)

def find_most_frequent_words(filepath, n=10):
    return find_most_common_words(filepath, n)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def remove_support_words(text, stopwords_file='./data/stop_words.txt'):
    with open(stopwords_file, 'r', encoding='utf-8') as f:
        stop_words = f.read().split()
    words = text.split()
    return [word for word in words if word not in stop_words]

def check_text_similarity(file1, file2, stopwords_file='./data/stop_words.txt'):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        text1 = clean_text(f1.read())
        text2 = clean_text(f2.read())
    words1 = set(remove_support_words(text1, stopwords_file))
    words2 = set(remove_support_words(text2, stopwords_file))
    intersection = words1 & words2
    union = words1 | words2
    similarity = len(intersection) / len(union) if union else 0
    return round(similarity * 100, 2)

def most_repeated_words(filepath, n=10):
    return find_most_common_words(filepath, n)

def hacker_news_analysis(filepath):
    python_count = 0
    javascript_count = 0
    java_only_count = 0
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            line = ' '.join(row)
            if re.search(r'\b[Pp]ython\b', line):
                python_count += 1
            if re.search(r'\b[Jj]ava[Ss]cript\b', line):
                javascript_count += 1
            elif re.search(r'\b[Jj]ava\b', line):
                java_only_count += 1
    return python_count, javascript_count, java_only_count

speeches = [
    'obama_speech.txt',
    'michelle_obama_speech.txt',
    'donald_speech.txt',
    'melina_trump_speech.txt'
]
for speech in speeches:
    path = f'./data/{speech}'
    lines, words = count_lines_words(path)
    print(f"{speech}: {lines} lines, {words} words")

print(most_spoken_languages('./data/countries_data.json', 10))
print(most_spoken_languages('./data/countries_data.json', 3))

print(most_populated_countries('./data/countries_data.json', 10))
print(most_populated_countries('./data/countries_data.json', 3))

emails = extract_emails('./data/email_exchange_big.txt')
print(emails[:10])  

print(find_most_common_words('./data/sample.txt', 10))
print(find_most_common_words('./data/sample.txt', 5))

print(find_most_frequent_words('./data/obama_speech.txt'))
print(find_most_frequent_words('./data/michelle_obama_speech.txt'))
print(find_most_frequent_words('./data/donald_speech.txt'))
print(find_most_frequent_words('./data/melina_trump_speech.txt'))

similarity = check_text_similarity('./data/michelle_obama_speech.txt', './data/melina_trump_speech.txt')
print(f"Similarity: {similarity}%")

print(most_repeated_words('./data/romeo_and_juliet.txt'))
python, js, java_only = hacker_news_analysis('./data/hacker_news.csv')
print(f"Python: {python}, JavaScript: {js}, Java Only: {java_only}")