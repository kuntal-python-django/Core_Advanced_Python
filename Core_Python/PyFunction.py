# def M1():
#     print("I m M1")

# M1()

# def M2(x=1, y=2):
#     print(x+y)

# M2()
# M2(7)
# M2(5, 5)


# def M3():
#     return 1

# print(M3())

# def M4():
#     return 1, 2, 3

# x, y, z = M4()
# print(M4())

# Generator Function
def M5():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


def M6():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
    yield 'E'


for i in M6():
    print(i)