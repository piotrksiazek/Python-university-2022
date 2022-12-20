from random import choice

class QueueEmptyException(Exception):
    pass

class QueueFullException(Exception):
    pass

class RandomQueue:
    def __init__(self, size=5):
        self.items = []
        self.indices = {}
        self.size = size

    def insert(self, item):
        if self.is_full():
            raise QueueFullException("cannot insert to a full queue")

        self.items.append(item)
        self.indices[item] = len(self.items) - 1

    def remove(self):
        if self.is_empty():
            raise QueueEmptyException("cannot remove from epmty queue")

        item = choice(self.items)
        index = self.indices[item]
        self.items[index] = self.items[-1]
        self.indices[self.items[index]] = index

        del self.items[-1]
        del self.indices[item]

        return item

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

    def clear(self):
        self.items = []
        self.indices = {}