dog = {}
dog['name'] = 'Maru'
dog['color'] = 'Black'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3

student = {
    'first_name': 'keith',
    'last_name': 'parrocha',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'Communication'],
    'country': 'Philippines',
    'city': 'LU',
    'address': 'aringay'
}

print("Length of student dictionary:", len(student))

skills = student['skills']
print("Skills:", skills)
print("Type of skills:", type(skills))  

student['skills'].append('Data Analysis')
student['skills'].append('Public Speaking')
keys = list(student.keys())
print("Keys:", keys)

values = list(student.values())
print("Values:", values)
items = list(student.items())
print("Items as list of tuples:", items)

del student['marital_status']

del dog 