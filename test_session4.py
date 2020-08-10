import subprocess
import sys
    
import pytest
import time
import os.path
import re
import inspect 
import session4
from session4 import Qualean

README_CONTENT_CHECK_FOR = [
    '__init__'
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__', 
    '__gt__', 
    '__invertsign__', 
    '__le__', 
    '__lt__', 
    '__mul__', 
    '__sqrt__', 
    '__bool__'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

    
def test_class_repr():
    a = Qualean(1)
    b = Qualean(0)
    c = Qualean(-1)

    assert 'object at' not in a.__repr__() and 'object at' not in b.__repr__() and 'object at' not in c.__repr__()

def test_fourspace():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"

def test_add():
    ''' Test for addition of Qualean Objects
    '''
    a = Qualean(1)
    b = Qualean(-1)
    c = a.__add__(b)
    assert c == a + b, "Addition implemented incorrectly"

def test_mul():
    ''' Test for multiplication of Qualean Objects
    '''
    a = Qualean(1)
    b = Qualean(-1)
    c = a.__mul__(b)
    assert c == a * b, "Multiplication implemented incorrectly"

def test_logical_and():
    '''Test for and'''
    a = Qualean(0)
    b = Qualean(1)
    assert a and b == False




if __name__ ==  '__main__':
    test_fourspace()
