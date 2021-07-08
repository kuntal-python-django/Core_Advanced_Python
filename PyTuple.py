t = ('A', 'B', 1, 2, 3)
print(type(t))
print(t)
print(len(t))
print(t[0])
print(t[-1])
print(t[1:3])

# Another Way to create Tuple
names = 'Jeff', 'Bill', 'Steve', 'Yash'
print(names)


# Tuple Operations
t1=(1,2,3)
t2=(4,5,6)     
t3 = t1+t2
print(t3) # >> (1, 2, 3, 4, 5, 6) 
t4 = t2+(7,)
print(t4) # >> (4, 5, 6, 7)
t5 = t1*4
print(t5) # >> (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)