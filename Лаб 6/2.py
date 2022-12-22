n = int(input("Число:"))

def func1(n):
    return lambda: n*2

def func2(func1):
    return func1() * 5

print("Введите N")
print(func2(func1(n)))