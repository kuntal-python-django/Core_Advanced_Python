l = [1, 2, 3,'A', 'X', 3.5]
print(l)

print(len(l))
l.append('W')
print(l)

print(l.pop())
print(l)

l1 = [1, 2, 3]
l.extend(l1)
print(l)


x = [i for i in range(10)]
print(x)

y = [i for i in range(10) if i%2==0]
print(y)
