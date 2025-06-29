from math import sqrt
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        middle = n // 2
        if n % 2 == 0:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        return sorted_data[middle]

    def mode(self):
        freq = Counter(self.data)
        mode_val, count = freq.most_common(1)[0]
        return {'mode': mode_val, 'count': count}

    def var(self):
        mean = self.mean()
        return round(sum((x - mean) ** 2 for x in self.data) / self.count(), 1)

    def std(self):
        return round(sqrt(self.var()), 1)

    def freq_dist(self):
        freq = Counter(self.data)
        return sorted([(count * 100 / self.count(), key) for key, count in freq.items()], reverse=True)

    def describe(self):
        print("Count:", self.count())
        print("Sum: ", self.sum())
        print("Min: ", self.min())
        print("Max: ", self.max())
        print("Range: ", self.range())
        print("Mean: ", self.mean())
        print("Median: ", self.median())
        print("Mode: ", tuple(self.mode().values()))
        print("Variance: ", self.var())
        print("Standard Deviation: ", self.std())
        print("Frequency Distribution:", self.freq_dist())

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
        33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
data.describe()

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {} 
        self.expenses = {} 

    def add_income(self, description, amount):
        self.incomes[description] = self.incomes.get(description, 0) + amount

    def add_expense(self, description, amount):
        self.expenses[description] = self.expenses.get(description, 0) + amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        info = f"Account Holder: {self.firstname} {self.lastname}\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Account Balance: {self.account_balance()}"
        return info

person = PersonAccount('keith', 'lucena')
person.add_income('Salary', 5000)
person.add_income('Freelance', 1500)
person.add_expense('Rent', 1200)
person.add_expense('Groceries', 500)

print(person.account_info())