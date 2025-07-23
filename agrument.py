
def addition ( a, b):
    return a + b;

result  = addition(5, 10)
print("Addition result:", result)


def new_func(*args):
    print("Arguments received:", args)
    return sum(args)

data = new_func(1, 2, 3, 4, 5)
