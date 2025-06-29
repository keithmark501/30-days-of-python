import math
age = 21
height = 1.75
complex_number = 3 + 4j
base = float(input("Enter base:"))
triangle_height = float(input("Enter height:"))
area = 0.5 * base * triangle_height
print("The area of the triangle is:", area)

a = float(input("Enter side a:"))
b = float(input("Enter side b:"))
c = float(input("Enter side c:"))
perimeter = a + b + c
print("The perimeter of the triangle is:", perimeter)

length = float(input("Enter lengt:"))
width = float(input("Enter width:"))
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
print("Area:", rectangle_area)
print("Perimeter:", rectangle_perimeter)

radius = float(input("Enter radius:"))
pi = 3.14
circle_area = pi * radius ** 2
circumference = 2 * pi * radius
print("Area of circle:", circle_area)
print("Circumference of circle:", circumference)

slope = 2
x_intercept = 2 / 2 # y =0 -> 2x -2 =0 -> x = 1
y_intercept = -2
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
distance = math.sqrt ((x2 - x1)**2 + (y2 - y1)**2)
print("Slope between points:", slope_2)
print("Euclidean distance:", distance)
print("Slopes are equal?", slope == slope_2)

for x in range(-10, 10):
    y = x**2 +6*x + 9
    if y == 0:
        print(f"y is zero when x = {x}")
        break

    print(len("python") != len ("meow"))
print('on' in 'python' and 'on' in 'meow')
print('meow' in ' I hope this course is not full of meow.')
print('on' not in 'meow' and 'on' not in 'python')

text_length = len("python")
print(float(text_length))
print(str(text_length))

number = int(input("Enter a number to check even/odd:"))
print("Even?", number % 2 == 0)
print(7 // 3 == int (2.7))
print(type('10') == type(10))

try:
    print(int('9.8') ==10) 
except ValueError as e:
    print("Error:", e)

    hours =float(input("Enter hours:"))
    rate = float(input("Enter rate per hour:"))
    pay = hours * rate
    print("Your weekly earning is:", pay)

years = int(input("Enter number of years you have lived:"))
seconds_lived = years * 365 * 24 * 60 * 60
print("You have lived for", seconds_lived, "seconds") 

print ("Number 1 Number 2 Number 3")
print(1, 1, 1, 1**2, 1**3)
print(2, 1, 2, 2**2, 2**3)
print(3, 1, 3, 3**2, 3**3)
print(4, 1, 4, 4**2, 4**3)
print(5, 1, 5, 5**2, 5**3)