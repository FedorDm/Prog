x = int(input("Число:"))

def function(x):
    def f(x):
        return (x)
    return(f(x) * x)
print(function(x))