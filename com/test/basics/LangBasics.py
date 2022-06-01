def func():
    s = 0
    for i in range(10):
        s = s + i
    return s


print(func())


def func1():
    s1 = 0
    for i in range(10):
        s1 += i
        yield s1
for i1 in func1():
    print(i1)
