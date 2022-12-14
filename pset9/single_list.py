class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) 

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node   

    def __iter__(self):
        # Przy tworzeniu iteratora trzeba mieć zmiennć, która będzie pamiętać stan.
        # Przy kolejnym tworzeniu iteratora będzie ustawianie na początek.
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            node = self.current
            self.current = self.current.next
            return node.data
        else:   # self.current is None
            raise StopIteration

    next = __next__   # kompatybilność Py2 i Py3

    def __eq__(self, other):
        if self.length != other.length:
            return False

        current = self.head
        otherCurrent = other.head
        while current != None:
            if current.data != otherCurrent.data:
                return False
            current = current.next
            otherCurrent = otherCurrent.next
        return True

    def search(self, data):   # klasy O(n)
        current = self.head
        while current != None:
            if current.data == data:
                return current
            current = current.next
        return None

    def find_min(self):   # klasy O(n)
        if self.head == None:
            return None
        
        current = self.head
        min = current.data

        while current != None:
            if current.data < min:
                min = current.data
            current = current.next
        
        return min

    def find_max(self):
        if self.head == None:
            return None
        
        current = self.head
        min = current.data

        while current != None:
            if current.data > min:
                min = current.data
            current = current.next
        
        return min

    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next           
        self.head = previous