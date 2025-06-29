first_name = "keith"
last_name = "parrocha"
age = 21
is_student = True
print ("Data types:")
print("first_name:", type(first_name))
print("last_name:", type(last_name))
print("age:", type(age))
print("is_student:", type(is_student))

print("Length of first name:", len(first_name) )
print("First name is longer" if len(first_name) > len(last_name)else "Last name is longer" if len (last_name)> len(first_name)else "Both names are of equal length")

num_one =5
num_two =4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp =num_one ** num_two
floor_division = num_one // num_two
print("Math operations:")
print("total:", total)
print("diff:", diff)
print("product:", product)
print("division:", division)
print("remainder:", remainder)
print("exponentiation:", exp)
print("floor_division:", floor_division)
import math 
radius = 30
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius
user_radius = float(input("Enter radius to calculate area:"))
user_area = math.pi * user_radius ** 2
print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)
print("User input area:", user_area)

user_first_name = input("Enter your first name:")
user_last_name = input("Enter your last name:")
user_country = input("Enter your country:")
user_age = input("Enter your age:")

print("User info:")
print("First Name:", user_first_name)
print("Last Name:", user_last_name)
print("Country:", user_country)
print("Age:", user_age)

help('keywords')