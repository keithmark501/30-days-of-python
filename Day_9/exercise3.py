person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Python'],
    'address': {
        'street': 'Space Street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print("Skills:", person['skills'])

    skills = person['skills']
    middle_index = len(skills) // 2
    if len(skills) % 2 == 0:
        middle_skills = skills[middle_index - 1:middle_index + 1]
        print("Middle skills:", middle_skills)
    else:
        print("Middle skill:", skills[middle_index])
else:
    print("No skills listed.")

if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in Finland.")
else:
    print(f"{person['first_name']} {person['last_name']} is not married or does not live in Finland.")