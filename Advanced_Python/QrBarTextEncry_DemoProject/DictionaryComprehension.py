# L = {i for i in range(10)}
# print(L)


keys = ['a','b','c','d','e'] 
values = [1,2,3,4,5]   
 
# myDict = { k:v for (k,v) in zip(keys, values)} 
# print(myDict)

M = {i:j for i, j in zip(keys, values) if j%2 == 0}
print(M)
