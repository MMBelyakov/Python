class MyObject:
    int_field = 8
    str_field = "a string"


print(MyObject.int_field)
print(MyObject.str_field)

object1 = MyObject()
object2 = MyObject()

print(object1.int_field)
print(object2.str_field)

MyObject.int_field = 10
print(MyObject.int_field)
print(object1.int_field)

object1.str_field = "another string"
print(MyObject.str_field)
print(object1.str_field)
print(object2.str_field)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, "is", self.age)


John = Person("John", 22)
Lucy = Person("Lucy", 21)

print()
print(John.name, "is", John.age)
print(Lucy.name, "is", Lucy.age)

print()
Person.print_info(John)
Person.print_info(Lucy)

print()
John.print_info()
Lucy.print_info()


class MyObject:
    class_attribute = 8

    def __init__(self):
        self.data_attribute = 42

    def instance_method(self):
        print(self.data_attribute)

    @staticmethod
    def static_method():
        print(MyObject.class_attribute)


if __name__ == "__main__":
    MyObject.static_method()
    obj = MyObject()
    obj.instance_method()
    obj.static_method()


class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self):
        return "rectangle(%.1f,%.1f)" % (self.side_a, self.side_b)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return "circle (%.1f)" % self.radius

    @classmethod
    def from_rectangle(cls, rectangle):
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
        return cls(radius)


def main():
    rectangle = Rectangle(3, 4)
    print(rectangle)

    first_circle = Circle(1)
    print(first_circle)

    second_circle = Circle.from_rectangle(rectangle)
    print(second_circle)


if __name__ == "__main__":
    main()


# методы

class MyObject:

    def __init__(self):
        self.__private_atribute = 0

    def get_private(self):
        return self.__private_atribute

    def set_atribute(self, value):
        if value < 100:
            self.__private_atribute = value


obj = MyObject()
obj.set_atribute(30)
print(obj._MyObject__private_atribute)


# свойства

class MyObject:
    def __init__(self):
        self.__attribute = 0

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        if value < 100:
            self.__attribute = value


obj = MyObject()
obj.attribute = 200
print(obj.attribute)


class Complex:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return "Complex({!r} , {!r})".format(self.real, self.imaginary)

    def __str__(self):
        return "{}{:+d}i".format(self.real, self.imaginary)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __neg__(self):
        return Complex(-self.real, -self.imaginary)

    def __sub__(self, other):
        return self + (-other)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        self.value = "some value"


class MyObject:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        if item == "secret field" and self.password == "9ea)fc":
            return "secret value"
        else:
            return object.__getattribute__(self, item)
