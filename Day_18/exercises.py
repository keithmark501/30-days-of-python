from collections import Counter
import re

paragraph = '''I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the capabilities 
to develop an application what else can you love.'''

words = re.findall(r'\b\w+\b', paragraph.lower())
word_freq = Counter(words)
most_common = word_freq.most_common()

print("Most frequent words:\n", most_common)

import re

def is_valid_variable(var_name):
    return bool(re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', var_name))

print(is_valid_variable('first_name'))   
print(is_valid_variable('first-name'))   
print(is_valid_variable('1first_name'))  
print(is_valid_variable('firstname'))    

from collections import Counter
import re

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering 
peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. 
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    cleaned = re.sub(r'[^\w\s]', '', text)
    return cleaned

def most_frequent_words(text, n=3):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(n)

cleaned_text = clean_text(sentence)
print("Cleaned text:\n", cleaned_text)

top_words = most_frequent_words(cleaned_text)
print("Most frequent words:", top_words)