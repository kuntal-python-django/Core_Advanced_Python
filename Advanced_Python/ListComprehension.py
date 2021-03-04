# L = [i for i in range(10)]
# print(L)

# S = [x**2 for x in range(10)]
# print(S)

# V = [2**i for i in range(13)]
# print(V)

# L1 = [[i, i+1] for i in range(10)]
# print(L1)

# M = [x for x in range(10) if x % 2 == 0]
# print(M)

# divided = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]
# print(divided)

# X = [x for x in range(100) if x % 2 == 0 and x % 6 == 0]
# print(X)

Y = [x if x%2 == 0 else x+100 for x in range(20)]
print(Y)