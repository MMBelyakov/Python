def function():
    """Example function
    Some long definition.
    """
    print("function called")


function()
help(function)

print(function.__doc__)

# radix-change

number = int(input("Enter a number: "))
print("Binary: ", bin(number))
print(("Octal: ", oct(number)))
print(("Hexacedimal: ", hex(number)))

# reversed_example
for i in reversed('qaxgkdw'):
    print(i)

# min_max
a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

print("Min", min(a, b, c))
print("Max", max(a, b, c))


# nested_function
def outer_function():
    def inner_function():
        print("Inner function")

    print("Outer function")
    inner_function()


outer_function()


# scoping_example1

def function():
    global var
    var = 'new variable'
    print(var)


var = 'global variable'
function()
print(var)


# scopind_example2

def outer_function():
    var = 8

    def inner_function():
        global var
        print(var)
        var = 10

    print(var)
    inner_function()
    print(var)


var = 0
print(var)
outer_function()
print(var)


# factorial
def nonrecursive_factorial(n):
    result = 1
    for multipier in range(2, n + 1):
        result *= multipier
    return result


def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


print(recursive_factorial(994))


# fibonacci
# import functools

# @functools.lru_cache(maxsize=None)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 10):
    print(fib(i))


# index = int(input("Enter a fibonacci sequence index: "))
# print(fib(index))

# hanoi_tower
# noinspection PyShadowingNames
def hanoi(n, a, b, c):
    if n != 0:
        hanoi(n - 1, a, c, b)
        print("Transfer a ring from ", a, "to", c)
        hanoi(n - 1, b, a, c)


hanoi(8, 'A', 'B', 'C')
