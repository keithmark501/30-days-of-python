empty_list = []
items = ['apple', 'banana', 'cherry', 'grapes', 'orange', 'mango']
print(len(items))

first_item = items[0]
middle_item = items[len(items) // 2]
last_item = items[-1]
print(first_item, middle_item, last_item)

mixed_data_types = ['keith', 21, 5.8, 'single', 'aringay']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[len(it_companies) //2])
print(it_companies[-1])

it_companies[0] = 'Meta'
print(it_companies)
it_companies.append('Tesla')
print(it_companies)
it_companies.insert(len(it_companies)//2, 'Spotify')

for i in range(len(it_companies)):
    if it_companies[i].lower() !='ibm': it_companies[i] = it_companies[i].upper()
    break
print(it_companies)

joined_string = '#;'.join(it_companies)
print(joined_string)
print('GOOGLE' in it_companies)

it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[:3])
print(it_companies[-3:])

mid = len(it_companies) //2
if len(it_companies) %2 ==0:
    print(it_companies[mid-1 :mid+1])
else:
    print(it_companies[mid])

it_companies.pop(0)    
print(it_companies)
mid = len(it_companies) //2
it_companies.pop (mid)
print(it_companies)
it_companies.pop()
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

index_redux = full_stack.index('Redux')
full_stack.insert(index_redux + 1, 'Python')
full_stack.insert(index_redux + 2, 'SQL')
print(full_stack)