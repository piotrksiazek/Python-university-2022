import pytest

from random import choice

from random_queue import RandomQueue, QueueEmptyException, QueueFullException

def test_insert():
    queue = RandomQueue(size=5)

    for i in range(5):
        queue.insert(i)

    assert queue.is_full() == True
    with pytest.raises(QueueFullException):
        queue.insert(6)

def test_remove():
    queue = RandomQueue(size=5)

    for i in range(5):
        queue.insert(i)

    item = queue.remove()

    assert item in [0, 1, 2, 3, 4]
    assert queue.is_full() == False

def test_clear():
    queue = RandomQueue(size=5)

    for i in range(5):
        queue.insert(i)

    queue.clear()

    assert queue.is_empty() == True

def test_remove_empty_queue():
    queue = RandomQueue()

    with pytest.raises(QueueEmptyException):
        queue.remove()
