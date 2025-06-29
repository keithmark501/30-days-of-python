def evens_and_odds(n):
    evens = 0
    odds = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}\nThe number of evens are {evens}"

print(evens_and_odds(1234567890))

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("Factorial of 5 is", factorial(5))

def is_empty(item):
    return not bool(item)

print("Is empty:", is_empty(""))  
print("Is empty:", is_empty([1, 2]))  

from collections import Counter
import math

def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0

def calculate_median(lst):
    if not lst:
        return 0
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    else:
        return lst[mid]

def calculate_mode(lst):
    if not lst:
        return None
    count = Counter(lst)
    max_count = max(count.values())
    modes = [k for k, v in count.items() if v == max_count]
    return modes if len(modes) > 1 else modes[0]

def calculate_range(lst):
    return max(lst) - min(lst) if lst else 0

def calculate_variance(lst):
    if not lst:
        return 0
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))
data = [1, 2, 3, 4, 4, 5, 5, 5]

print("Mean:", calculate_mean(data))
print("Median:", calculate_median(data))
print("Mode:", calculate_mode(data))
print("Range:", calculate_range(data))
print("Variance:", calculate_variance(data))
print("Standard Deviation:", calculate_std(data))