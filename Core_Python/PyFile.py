# Write
# ['a', 'w']
f = open("demo.txt", 'a')
data = input('Enter Some Data :')
f.write(data)
f.close()


# Read
f = open("demo.txt", 'r')
print(f.read())
print(f.readline())
print(f.readlines())
print(f.read(10))
f.close()
