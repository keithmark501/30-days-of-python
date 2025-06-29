age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    print(f"You need {18 - age} more year{'s' if 18 - age > 1 else ''} to be able to drive.")

my_age = 25  
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    print(f"You are {diff} year{'s' if diff > 1 else ''} older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    print(f"I am {diff} year{'s' if diff > 1 else ''} older than you.")
else:
    print("We are the same age.")

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")