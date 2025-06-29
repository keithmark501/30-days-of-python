ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Sorted ages:", ages)
min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age)
print("Max age:", max_age)

ages.append(min_age)
ages.append(max_age)
print("Ages after adding min and max again:", ages)
ages.sort()  
n = len(ages)
if n % 2 == 0:
    median = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    median = ages[n // 2]
print("Median age:", median)


average = sum(ages) / len(ages)
print("Average age:", average)
age_range = max_age - min_age
print("Age range:", age_range)

min_diff = abs(min_age - average)
max_diff = abs(max_age - average)
print("Abs(min - avg):", min_diff)
print("Abs(max - avg):", max_diff)

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid_index = len(countries) // 2
if len(countries) % 2 == 0:
    print("Middle countries:", countries[mid_index - 1:mid_index + 1])
else:
    print("Middle country:", countries[mid_index])

if len(countries) % 2 == 0:
    first_half = countries[:mid_index]
    second_half = countries[mid_index:]
else:
    first_half = countries[:mid_index + 1]
    second_half = countries[mid_index + 1:]
print("First half:", first_half)
print("Second half:", second_half)

first, second, third, *scandic_countries = countries
print("First three countries:", first, second, third)
print("Scandic countries:", scandic_countries)


