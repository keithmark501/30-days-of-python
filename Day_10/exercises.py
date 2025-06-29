print("For loop 0 to 10:")
for i in range(11):
    print(i)

print("While loop 0 to 10:")
i = 0
while i <= 10:
    print(i)
    i += 1

print("For loop 10 to 0:")
for i in range(10, -1, -1):
    print(i)

print("While loop 10 to 0:")
i = 10
while i >= 0:
    print(i)

    i -= 1
for i in range(1, 8):
    print('#' * i)
print("Nested loop triangle:")
for i in range(1, 6):
    for j in range(i):
        print('#', end='')
    print()

for i in range(11):
    print(f"{i} * {i} = {i * i}")

tools = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tool in tools:
    print(tool)

for i in range(0, 101):
    if i % 2 == 0:
        print(i)
for i in range(0, 101):
    if i % 2 != 0:
        print(i)
total_sum = sum(range(101))
print(f"The sum of all numbers is {total_sum}")
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"The sum of all evens is {even_sum}")
print(f"The sum of all odds is {odd_sum}")

from data.countries import countries  
land_countries = [country for country in countries if 'land' in country]
print("Countries containing 'land':", land_countries)

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print("Reversed fruits:", reversed_fruits)

from data.countries_data import countries_data  
all_languages = set()
for country in countries_data:
    all_languages.update(country['languages'])
print("Total number of languages:", len(all_languages))
from collections import Counter

language_counter = Counter()
for country in countries_data:
    language_counter.update(country['languages'])

most_spoken = language_counter.most_common(10)
print("Ten most spoken languages:")
for lang, count in most_spoken:
    print(f"{lang}: {count} countries")

most_populated = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]
print("Ten most populated countries:")
for country in most_populated:
    print(f"{country['name']}: {country['population']}")