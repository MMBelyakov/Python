# raise ValueError('invalid argument')
print('Calculator')

try:
    a = float(input('a = '))
    b = float(input('b = '))
    print(a / b)
# except ZeroDivisionError:
#   print("division by zero")
except (ZeroDivisionError, ValueError) as error:
    print(error)

print('Stopping the calculator.')
input()

Max_stars = 30
width = 80


def print_result(number):
    if number == 0:
        stars_count = Max_stars
    else:
        stars_count = round(Max_stars / number)
        if stars_count > Max_stars:
            stars_count = Max_stars

    number_field_width = width - 2 * stars_count
    stars = '*' * stars_count
    fmt = '{0}{1:^' + str(number_field_width) + '}{0}'

    print(fmt.format(stars, number))


def main():
    while True:
        try:
            first_number = float(input('First number : '))
            second_number = float(input('Second number :'))
            result = first_number / second_number
        except (ZeroDivisionError, ValueError) as error:
            print('Error: ', error)
            print('Please try again')
            print()
        else:
            print_result(result)
            break


if __name__ == '__main__':
    main()

try:
    3 / 0
except:
    pass

print('program flows further')


class Myobject:
    def __del__(self):
        print(self, 'is about to be deleted')


obj = Myobject()
del obj


class ObjectWithDestructor:
    def __del__(self):
        print('destructor invoked')
        raise Exception


print('Creating object ...')
obj = ObjectWithDestructor()

print('Deleting reference ...')
del obj

print('Done')


def do_stuff():
    try:
        raise ValueError
    except ZeroDivisionError:
        print('division by zero')


try:
    do_stuff()
except ValueError:
    print('value error')


def main():
    try:
        raise ValueError('value is incorrect')
    except ValueError as error:
        print('Exception: ', error)
        raise


try:
    main()
except ValueError:
    print('ValueError detected')

try:
    raise ValueError
except ValueError:
    raise ZeroDivisionError

value_error = ValueError()
value_error.__cause__ = ZeroDivisionError()
raise value_error

raise ValueError from ZeroDivisionError

a = 5
b = 0
try:
    result = a / b
except ZeroDivisionError as error:
    raise ValueError('variable b is incorrect') from error


def fn():
    try:
        return
    # raise ZeroDivisionError
    finally:
        print('finally block')


fn()

import warnings

name = input('Enter your first and last name')

if name.count(' ') != 1:
    warnings.warn('Name format may be incorrect')

print('Hello ', name, '!', sep='')
