class Base:
    def method(self):
        print("Hello!")


class Child(Base):
    def child_method(self):
        print("Hello from child method")

    def method(self):
        print("Hello from redefined method")


obj = Child()
obj.method()
obj.child_method()


class figure:
    def __init__(self, side=0.0):
        self.side = side


class Square(figure):
    def draw(self):
        for i in range(self.side):
            print('* ' * self.side)


class Triangle(figure):
    def draw(self):
        for i in range(1, self.side + 1):
            print("* " * i)


def main():
    square = Square(5)
    triangle = Triangle(8)
    square.draw()
    print()
    triangle.draw()


if __name__ == '__main__':
    main()


class Horse:
    def run(self):
        print("I'm  running.")


class Bird:
    def fly(self):
        "I'm  flying."


class Pegasus(Horse, Bird):
    pass


def main():
    pegasus = Pegasus()
    pegasus.run()
    pegasus.fly()


if __name__ == "__main__":
    main()


class Myobject(object):
    pass


print(type(Myobject))


class Myobject:
    pass


print(type(Myobject))


class Base:
    def method(self):
        print("Method class:", __class__.__name__)
        print("Instance class", type(self).__name__)


class Child(Base):
    pass


if __name__ == "__main__":
    base_instance = Base()
    base_instance.method()

    child_instance = Child()
    child_instance.method()


class A:
    def method(self):
        print("A method")


class B(A):
    pass


class C(A):
    def method(self):
        print("C method")


class D(B, C):
    pass


obj = D()
obj.method()

print(D.mro())
for cls in [A, B, C, D]:
    print(cls.__name__ + ":", cls.mro())


class MethodContainer:
    def __init__(self, data):
        self.data = data

    def method(self):
        print('method invoked')
        print('data = ', self.data)


instance = MethodContainer(8)

print(type(MethodContainer.method))
print(type(instance.method))
MethodContainer.method(instance)


class Base:
    def method(self):
        print('Base method invoked on ', type(self).__name__, 'instance')


class Child(Base):
    def method(self):
        super().method()
        # Base.method(self)
        print('Child method invoked on ', type(self).__name__, 'instance')


base_instance = Base()
base_instance.method()

child_instance = Child()
child_instance.method()


# Base.method(child_instance) #метод класса Base вызван экземпляре класса child

class animal(object):
    def __init__(self):
        self.can_run = False
        self.can_fly = False

    def print_abilities(self):
        print(type(self).__name__ + ":")
        print('Can run :', self.can_run)
        print('Can fly:', self.can_fly)
        print()


class Horse(animal):
    def __init__(self):
        super().__init__()
        self.can_run = True


class Bird(animal):
    def __init__(self):
        super().__init__()
        self.can_fly = True


class Pegasus(Horse, Bird):
    pass


if __name__ == '__main__':
    horse = Horse()
    horse.print_abilities()

    bird = Bird()
    bird.print_abilities()

    pegasus = Pegasus()
    pegasus.print_abilities()


def check_instasnce(obj, cls):
    return check_subclass(type(obj), cls)


def check_subclass(child, base):
    # return base in child.mro()
    if child == base:
        return True

    for direct_base in child.__bases__:
        if base == direct_base:
            return True
        return check_subclass(direct_base, base)
    return False


print(check_instasnce(8, int))
print(check_subclass(bool, object))
