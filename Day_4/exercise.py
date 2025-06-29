print(','.join(['Thirty', 'Days', 'of', 'Python']))
print(''.join(['Coding', 'For', 'All']))
company = "Coding For All" 
print (company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print(company.find('Coding') != -1)
print(company.replace('Coding', 'Python'))
print('Python for Everyone'.replace('Everyone', 'All'))
print(company.split())
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))
print(company[0])
print(len(company)-1)
print(company[10])

phrase1 ='Python for Everyone'
acronym1 = ''.join ([word[0] for word in phrase1.split()])
print(acronym1)
phrase2 = 'Coding for All'
acronym2 = ''.join([word[0] for word in phrase2.split()])
print(acronym2)

print(company.index('C'))
print(company.index('F'))
print("Coding For All".rfind('I'))
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rindex('because'))
start = sentence.find('because')
end = sentence.rindex('because')
len('because')
print(sentence[start:end])
print(sentence.find('because'))
print(sentence[start:end])
print(company.startswith('Coding'))
print(company.endswith('coding'))
print(company.strip())

print("30DaysofPython".isidentifier())
print("thirty_days_of_python".isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(libraries))
print("I am enjoying this challenge\nI just wonder what is next.")
print("Name\tAge\nAsabeneh\t250\nCountry\tfinland")

radius = 10 
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:. 2f}". format(radius, area))

a = 8
b = 6
print(f"{a} + {b} ={a + b}")
print(f"{a} - {b} ={a - b}")
print(f"{a} * {b} ={a * b}")
print(f"{a} / {b} ={a / b:.2f}")
print(f"{a} % {b} ={a % b}")
print(f"{a} // {b} ={a // b}")
print(f"{a} ** {b} ={a ** b}")
