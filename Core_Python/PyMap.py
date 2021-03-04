l1 = [1, 2, 3, 4, 5]
l2 = [5, 4, 3, 2, 1]
l3 = [5, 4, 3, 2, 1]

# for i in range(len(l1)):
#     print(l1[i]+l2[i]+l3[i])

# p = []

def cal(a=0, b=0, c=0):
    print(a+b+c)
    # p.append(a+b+c)

x = map(cal, l1, l2, l3)
# print(x)
x = list(x)
# print(p)
