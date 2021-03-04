# list comprehenision

# for i in range(10):
#     print(i)

# m = [i for i in range(10) if i%2==0]
# print(m)

# p = [[i, i+1] for i in range(10)]
# print(p)

# s = [x if x%2==0 else x**5 for x in range(10)]
# print(s)



# k = ["A", "B", "C", "D"]
# d1 = {i:j for i, j in enumerate(k)}
# print(d1)

# keys  = ["A", "B", "C", "D"]
# values = [1, 2, 3, 4]

# d = {k:v for (k,v) in zip(keys, values) if v%2==0}
# print(d)



# File Read Write
# Write
# ["a", "w"]
# f = open("a.txt", "a")
# data = input("Enter Data :")
# f.write(data)
# f.close() 

# f = open("a.txt", "r")
# print(f.read())
# print(f.read(6))
# print(f.readlines())