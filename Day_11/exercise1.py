import math

def add_two_numbers(a, b):
    return a + b
def area_of_circle(radius):
    return math.pi * radius * radius

def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    else:
        return "All items must be numbers."

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return "Autumn"
    elif month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    else:
        return "Invalid month"

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Undefined (division by zero)"
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)

def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst
def capitalize_list_items(lst):
    return [str(item).capitalize() for item in lst]

def add_item(lst, item):
    lst.append(item)
    return lst
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def sum_of_numbers(n):
    return sum(range(n + 1))

def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)