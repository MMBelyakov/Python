def print_numbers(limit):
    for i in range(limit):
        print(i)


n = int(input("n = "))
print_numbers(n)


# example1
def hello():
    print("Hello , World")
    print("This text gets printed from the function")
    print()


hello()
hello()


# example2
# import example1
def print_numbers(limit):
    # example1.hello()
    for i in range(limit):
        print(i)


def main():
    print_numbers(3)
    print()
    print_numbers(5)


if __name__ == " __main__":
    main()


# example3

def add_number(first, second):
    print("add_numbers called with", first, second)
    return first + second


add_number(9, 10)
result = add_number(2, 3) - add_number(1, 2)
print(result)


# example4

def function(x):
    if x < 0:
        return x * 2
    else:
        return x * 3


def main():
    for i in range(-3, 4):
        y = function(i)
        print('function(', i, ') = ', y, sep='')


main()


# example5

def print_info(object_name='unknown object', color='white', price=0):
    print('Object:', object_name, sep='\t')
    print('Color:', color, sep='\t')
    print('Price:', price, sep='\t')
    print()


print_info(color='red')

# print_info(object_name = 'pen',
#          color = 'blue',
#          price = 1
#         )
# print_info(price = 5 , object_name= 'cup' , color= 'orange')

print_info('coffee', price=10, color='black')


# example6
def hello(name='Alex'):
    print('Hello', name, '!', sep=' ')


hello()
