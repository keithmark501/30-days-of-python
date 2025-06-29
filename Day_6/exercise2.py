family_members = ('maring', 'josie', 'larry', 'kalbo', 'Father', 'Mother')
siblings = family_members[:-2]
parents = family_members[-2:]
print("Siblings:", siblings)
print("Parents:", parents)

fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'spinach', 'potato')
animal_products = ('dog', 'cat', 'horse')

food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff (tuple):", food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print("Food stuff (list):", food_stuff_lt)

n = len(food_stuff_lt)
if n % 2 == 0:
    middle_items = food_stuff_lt[n//2 - 1:n//2 + 1]
else:
    middle_items = [food_stuff_lt[n//2]]
print("Middle item(s):", middle_items)

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Is 'Estonia' a Nordic country?", 'Estonia' in nordic_countries)
print("Is 'Iceland' a Nordic country?", 'Iceland' in nordic_countries)