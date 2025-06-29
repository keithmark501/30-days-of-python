score = int(input("Enter your score: "))

if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 79:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
elif 0 <= score <= 49:
    print("Grade: F")
else:
    print("Invalid score. Please enter a number between 0 and 100.")

month = input("Enter the month: ").strip().capitalize()

if month in ['September', 'October', 'November']:
    print("The season is Autumn.")
elif month in ['December', 'January', 'February']:
    print("The season is Winter.")
elif month in ['March', 'April', 'May']:
    print("The season is Spring.")
elif month in ['June', 'July', 'August']:
    print("The season is Summer.")
else:
    print("Invalid month.")

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").strip().lower()

if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print("Fruit added. Updated list:", fruits)