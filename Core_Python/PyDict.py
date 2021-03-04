a = {'key': "value"}

a = {1: 'A', 2: 'B', 3: 'C'}
print(a)

print(a.keys())
print(a.values())

print(len(a))

keys = [1, 2, 3]
values = ['A', 'B', 'C']

d1 = {k:v for (k,v) in zip(keys, values)}
print(d1)
