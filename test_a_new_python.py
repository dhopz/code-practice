import pytest
from a_new_python import NewClass

@pytest.fixture
def new_class():
    return NewClass()

def test_get_new_class(new_class):
    # new_class = NewClass()
    assert new_class.list_of_strings == []
    assert new_class.an_integer == 0

def test_create_new_class_with_parameters():
    new_class = NewClass(['this','is','a','new','class'],5)
    assert new_class.list_of_strings == ['this','is','a','new','class']

def test_if_array_times_an_integer():
    new_class = NewClass(['this','is','a','new','class'],2)
    assert new_class.do_something_in_class() == ['this', 'is', 'a', 'new', 'class', 'this', 'is', 'a', 'new', 'class']

def test_return_a_dictionary(new_class):
    new_class = NewClass(['this','is','a','new','class'])
    assert new_class.create_json() == {'new_json':['this','is','a','new','class']}