import pandas as pd

file_path = 'data/hacker_news.csv'
df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

titles = df['title']
print("\nTitle column (as Series):")
print(titles.head())

print("\nNumber of rows and columns:")
print(df.shape)

python_titles = df[df['title'].str.contains('python', case=False, na=False)]
print(f"\nNumber of titles containing 'python': {len(python_titles)}")
print(python_titles['title'].head())

js_titles = df[df['title'].str.contains('javascript', case=False, na=False)]
print(f"\nNumber of titles containing 'JavaScript': {len(js_titles)}")
print(js_titles['title'].head())

print("\nTop 10 most common words in titles:")

all_text = ' '.join(titles.dropna().astype(str)).lower()

from collections import Counter
import re

words = re.findall(r'\b\w+\b', all_text)
word_counts = Counter(words)
common_words = word_counts.most_common(10)

for word, count in common_words:
    print(f"{word}: {count}")