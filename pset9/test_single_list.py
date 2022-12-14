import pytest
from single_list import SingleList, Node

def getTestList():
    alist = SingleList()
    alist.insert_head(Node(11))         
    alist.insert_head(Node(22))        
    alist.insert_tail(Node(33))
    alist.insert_tail(Node(2))   
    alist.insert_tail(Node(1))   
    alist.insert_tail(Node(3))
    alist.insert_tail(Node(-2))   
    alist.insert_tail(Node(1))   
    alist.insert_tail(Node(-3))
    alist.insert_tail(Node(0))   
    alist.insert_tail(Node(1))   
    alist.insert_tail(Node(13))   
    return alist

def test_search_exists():
    assert getTestList().search(1).data == 1

def test_search_doesnt_exist():
    assert getTestList().search(420) == None

def test_find_min_non_empty_list():
    assert getTestList().find_min() == -3

def test_find_min_empty_list():
    assert SingleList().find_min() == None

def test_find_max_non_empty_list():
    assert getTestList().find_max() == 33

def test_find_max_empty_list():
    assert SingleList().find_max() == None

def test_eq():
    assert getTestList() == getTestList()

def test_eq_should_not_be_equal():
    list1 = getTestList()
    list2 = getTestList()
    list2.insert_tail(1)

    assert list1 != list2

def test_reverse():
    alist = SingleList()
    alist.insert_head(Node(1))    
    alist.insert_tail(Node(2))
    alist.insert_tail(Node(3))   
    alist.insert_tail(Node(4))     

    alist.reverse()

    alist1 = SingleList()
    alist1.insert_head(Node(4))    
    alist1.insert_tail(Node(3))
    alist1.insert_tail(Node(2))   
    alist1.insert_tail(Node(1))     

    assert alist1 == alist

def test_reverse_single_element():
    alist = SingleList()
    alist.insert_head(Node(1))

    alist1 = SingleList()
    alist1.insert_head(Node(1))

    alist.reverse()

    assert alist == alist1

def test_reverse_only_inserting_tails():
    alist = SingleList()
    alist.insert_tail(Node(1))    
    alist.insert_tail(Node(2))
    alist.insert_tail(Node(3))   
    alist.insert_tail(Node(4))     

    alist.reverse()

    alist1 = SingleList()
    alist1.insert_tail(Node(4))    
    alist1.insert_tail(Node(3))
    alist1.insert_tail(Node(2))   
    alist1.insert_tail(Node(1))     

    assert alist1 == alist

def test_reverse_only_inserting_heads():
    alist = SingleList()
    alist.insert_head(Node(1))    
    alist.insert_head(Node(2))
    alist.insert_head(Node(3))   
    alist.insert_head(Node(4))     

    alist.reverse()

    alist1 = SingleList()
    alist1.insert_head(Node(4))    
    alist1.insert_head(Node(3))
    alist1.insert_head(Node(2))   
    alist1.insert_head(Node(1))     

    assert alist1 == alist
