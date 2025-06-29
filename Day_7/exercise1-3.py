it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24}
age = [22, 19, 24, 25, 26, 24, 25]

print("Length of it_companies:", len(it_companies))
it_companies.add('Twitter')
print("After adding Twitter:", it_companies)
it_companies.update(['Tesla', 'Netflix', 'Airbnb'])
print("After adding multiple companies:", it_companies)

it_companies.remove('IBM')  
print("After removing IBM:", it_companies)

joined = A.union(B)
print("Joined A and B:", joined)
intersection = A.intersection(B)
print("A intersection B:", intersection)
print("Is A subset of B?", A.issubset(B))
print("Are A and B disjoint?", A.isdisjoint(B))
print("A union B:", A.union(B))
print("B union A:", B.union(A))
print("Symmetric difference between A and B:", A.symmetric_difference(B))

del A
del B

age_set = set(age)
print("Length of age list:", len(age))
print("Length of age set:", len(age_set))
print("Which is bigger? Age list is bigger." if len(age) > len(age_set) else "Age set is bigger or equal.")

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))
print("Unique words:", unique_words)