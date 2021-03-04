a = [1,2,3,4,5]
b = {1: 'A', 2: 'B'}

for i in range(len(a)):
    print(a[i])

for i in a:
    print(i)


for i in b:
    print(i, "-->", b[i])