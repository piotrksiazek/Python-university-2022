import pytest
from stack import Stack, StackEmptyException, StackFullException, ValueNotInRange

def test_stack_init():
    stack = Stack()
    assert stack.size == 10
    assert stack.is_empty() == True
    assert stack.is_full() == False

def test_stack_push():
    stack = Stack()
    stack.push(5)
    assert stack.items[0] == 5
    assert stack.is_empty() == False
    assert stack.is_full() == False

def test_stack_push_full():
    stack = Stack(size=1)
    stack.push(0)
    with pytest.raises(StackFullException):
        stack.push(1)

def test_stack_pop():
    stack = Stack()
    stack.push(5)
    stack.push(6)
    assert stack.pop() == 6
    assert stack.pop() == 5

def test_stack_pop_empty():
    stack = Stack()
    with pytest.raises(StackEmptyException):
        stack.pop()

def test_stack_push_invalid_type():
    stack = Stack()
    with pytest.raises(ValueError):
        stack.push("string")

def test_stack_push_out_of_range():
    stack = Stack()
    with pytest.raises(ValueNotInRange):
        stack.push(-1)
    with pytest.raises(ValueNotInRange):
        stack.push(10)

def test_stack_push_duplicate():
    stack = Stack()
    stack.push(5)
    stack.push(5)
    assert stack.items.count(5) == 1
    assert stack.presence[5] == True