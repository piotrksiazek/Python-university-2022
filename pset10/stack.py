#zadanie 10.2 oraz 10.3

class ValueNotInRange(Exception):
    def __init__(self, value, size):
        self.message = f'{value} must be >= 0 and < {size}'
        super().__init__(self.message)


class StackEmptyException(Exception):
    pass

class StackFullException(Exception):
    pass

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]
        self.presence = size * [False]
        self.n = 0                     
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise StackFullException
        if not isinstance(data, int):
            raise ValueError("data must be of type int")
        if data < 0 or data >= self.size:
            raise ValueNotInRange(data, self.size)
        if self.presence[data] is True:
            print("trying to insert duplicate")
            return
        self.items[self.n] = data
        self.presence[data] = True
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise StackEmptyException
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None
        self.presence[data] = False
        return data