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


if result is not None:
    print('Result: ', result)
z=math.ceil(1.11)
q=math.floor(1.11)
print(z,q)
