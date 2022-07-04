print("Hello, World !")

name ='Max'
print(name)
print("Hello, World !" )

name = input('What is your name ?')
print('Hello', name)

x = float(input('First number: '))
y = float(input('Second number: '))
operation = input('Operation: ')

import math
result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
elif operation == '**':
    result = x ** y
else: print('Unsupported operation')
