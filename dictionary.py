
#{}
#key value pair
# immutable

a = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

print("Dictionary:", type(a))

for i in a:
    print(i, ":", a[i])

for i in a.values():
    print("Value:", i)


for i in a.keys():
    print("key:", i)

print("key 'name' exists:", 'name' in a)

n = a['name']
print("Value for key 'name':", n)

l  = [43,34,67,23,45,67,89]
m = ['age', 'name', 'city', 'country']

print(dict(zip(m, l)))