def my_for(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            value = next(it)
            callback(value)
        except StopIteration:
            break


def loop_body(value):
    print('next value received', value)


my_for(range(10), loop_body)


class SimpleIterable:
    def __getitem__(self, index):
        if 0 <= index <= 5:
            return index * 2
        else:
            raise IndexError


iterable = SimpleIterable()
for value in iterable:
    print(value)

import math


class MyRange:
    def __init__(self, first, second=None, step=1):
        self.step = None
        if second is None:
            self.start = 0
            self.end = first

        else:
            self.start = first
            self.end = second

        if step != 0:
            self.step = step

        else:
            raise ValueError('Step can not be zero')

        self.lenght = math.ceil((self.end - self.start) / self.step)

    def __len__(self):
        return self.lenght

    def __getitem__(self, index):
        if 0 <= index <= len(self):
            return self.start + index * self.step

        else:
            raise IndexError('range index out of range')

    def __iter__(self):
        return RangeIterator(self)

    def __repr__(self):
        return 'MyRange{} ,{} , {}'.format(self.start, self.end, self.step)


class RangeIterator:
    def __init__(self, range_instance):
        self.step = None
        self.step = None
        self.range = range_instance
        self.next_value = range_instance.start

    def __iter__(self):
        return self

    def __next__(self):
        if (self.next_value >= self.range.end and self.step > 0) or \
                (self.next_value <= self.range.end and self.step < 0):
            raise StopIteration
        result = self.next_value
        self.next_value += self.range.step

        return result


class List:
    class Node:
        __slots__ = ('value', 'next')

    class NodeIterator:
        def __init__(self, first):
            self._next_node = None
            self._next_node = None
            self._next_node = None
            self._next_ = first

        def __iter__(self):
            return self
            current = self.start
            for _ in range(len(self)):
                yield current
                current += self.step

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, iterable=None):
        self._head = None
        self._tail = None
        self._leng = None
        if iterable is not None:
            self.extend(iterable)

    def __len__(self):
        return self._leng

        self._leng += 1

    def __getitem__(self, index):
        if index < 0:
            index += len(self)

        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        node = self._head
        while node is not None:
            yield node.value
            node = node.next
        # return  List._NodeIterator(self._head)

    def extend(self, iterable):
        pass


if __name__ == '__main__':
    numbers = List(range(1000))
    for x in numbers:
        if x % 1000 == 0:
            print(x)


def generator():
    yield 'Hello'
    yield 'World'


generator()
g = generator()
next(g)
next(g)


def fibonacci(count):
    first, second = 0, 1
    for _ in range(count):
        yield second
        first, second = second, first + second


count = int(input('How many Fibonacci numbers to print?'))
for fib in fibonacci(count):
    print(fib)

"""def generator_function():
    for x in range(5):
        for y in range(3):
            if (x+y) % 2==0:
                yield  x*y  """

generator = (x * y for x in range(5) for y in range(3) if (x % y) % 2 == 0)
for value in generator:
    print(value)

print(sum(x ** 2 for x in range(10)))


def subgenerator():
    yield '[subgenerator] hello'
    yield '[subgenerator] world'


def generator():
    yield '[generator] start '
    yield from subgenerator()
    yield from range(10)
    yield ' [generator] end'


for value in generator():
    print(value)

import random
import asyncio


async def produce():
    while True:
        await asyncio.sleep(0.5)
        data = random.randint(1, 100)
        consumer.sent(data)
        return data


async def consume():
    sum_ = 0
    count = 0

    while True:
        data = yield
        print('Got datas:', data)

        sum += data
        count += 1

        print('Sum:', sum_)
        print('Average', sum / count)
        print()


async def another_task():
    while True:
        print()
        print('Hello from another task!')
        print()
        await asyncio.sleep(1)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    tasks = [consume(), another_task()]
    loop.run_until_complete(asyncio.wait(tasks))

    consumer = consume()
    task = another_task()

    while True:
        print('next iteration')
        next(consumer)
        next(task)
