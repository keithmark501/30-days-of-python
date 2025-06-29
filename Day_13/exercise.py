numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_and_zero = [n for n in numbers if n <= 0]
print("Negatives and zero:", negatives_and_zero)

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [item for sublist in list_of_lists for inner in sublist for item in inner]
print("Flattened list:", flattened)

tuples_list = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print("List of tuples:")
for t in tuples_list:
    print(t)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3].upper(), city.upper()] 
                       for [[(country, city)]] in countries]
print("Flattened country list:", flattened_countries)

dict_countries = [{'country': country.upper(), 'city': city.upper()} 
                  for [[(country, city)]] in countries]
print("List of dictionaries:", dict_countries)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for [[(first, last)]] in names]
print("Concatenated names:", full_names)

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
y_intercept = lambda x, y, m: y - m * x

m = slope(1, 2, 3, 6)
b = y_intercept(1, 2, m)
print(f"Slope: {m}, Y-intercept: {b}")