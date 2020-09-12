import inspect
import os
import re
import string

import session8
from session8 import *


def test_readme_exists():
    """
    Check if the README file exists
    :return: None
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test the length of the README file
    :return: None
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add at least 500 words"


def test_readme_file_for_formatting():
    """
    Tests the formatting for the README file
    :return: None
    """
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    """
    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
    :return: None
    """
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_q1_check_doc_str_length():
    """
    Test the closure q1_check_doc_str_length
    :return: None
    """
    test_func = q1_check_doc_str_length()
    assert test_func(q1_check_doc_str_length)
    assert not test_func(lambda x: x)


def test_q2_get_next_fib_number():
    """
    Test the closure q2_get_next_fib_number
    :return: None
    """
    fib_seq1 = q2_get_next_fib_number()
    fib_seq2 = q2_get_next_fib_number()

    assert fib_seq1() == 1
    assert fib_seq1() == 2
    assert fib_seq1() == 3
    assert fib_seq1() == 5

    assert fib_seq2() == 1
    assert fib_seq2() == 2


def test_q3_update_local_counts():
    """
    Test the closure q3_update_local_counts
    :return: None
    """
    user1_functions = q3_update_local_counts()

    assert user1_functions(print, 'None')[1] == {'add': 0, 'mul': 0, 'div': 0}
    assert user1_functions(add, 1, 2)[1] == {'add': 1, 'mul': 0, 'div': 0}
    assert user1_functions(add, 1, 2)[1] == {'add': 2, 'mul': 0, 'div': 0}
    assert user1_functions(add, 1, 2)[1] == {'add': 3, 'mul': 0, 'div': 0}
    assert user1_functions(add, 1, 2)[1] == {'add': 4, 'mul': 0, 'div': 0}
    assert user1_functions(mul, 1, 2)[1] == {'add': 4, 'mul': 1, 'div': 0}
    assert user1_functions(add, 1, 2)[1] == {'add': 5, 'mul': 1, 'div': 0}
    assert user1_functions(div, 1, 2)[1] == {'add': 5, 'mul': 1, 'div': 1}
    assert user1_functions(mul, 1, 2)[1] == {'add': 5, 'mul': 2, 'div': 1}
    assert user1_functions(print, 'None')[1] == {'add': 5, 'mul': 2, 'div': 1}


def test_q4_update_counts_global():
    """
    Test the closure q4_update_counts_global
    :return: None
    """
    user1_functions = q4_update_counts_global({'add': 0, 'mul': 0, 'div': 0})
    assert user1_functions(print, 'None')[1] == {'add': 0, 'mul': 0, 'div': 0}
    assert user1_functions(add, 1, 2)[1] == {'add': 1, 'mul': 0, 'div': 0}
    assert user1_functions(add, 1, 2)[1] == {'add': 2, 'mul': 0, 'div': 0}
    assert user1_functions(add, 1, 2)[1] == {'add': 3, 'mul': 0, 'div': 0}
    assert user1_functions(add, 1, 2)[1] == {'add': 4, 'mul': 0, 'div': 0}
    assert user1_functions(mul, 1, 2)[1] == {'add': 4, 'mul': 1, 'div': 0}
    assert user1_functions(add, 1, 2)[1] == {'add': 5, 'mul': 1, 'div': 0}
    assert user1_functions(div, 1, 2)[1] == {'add': 5, 'mul': 1, 'div': 1}
    assert user1_functions(mul, 1, 2)[1] == {'add': 5, 'mul': 2, 'div': 1}
    assert user1_functions(print, 'None')[1] == {'add': 5, 'mul': 2, 'div': 1}

    user2_functions = q4_update_counts_global({'add': 0, 'mul': 0, 'div': 6})
    assert user2_functions(print, 'None')[1] == {'add': 0, 'mul': 0, 'div': 6}
    assert user2_functions(add, 1, 2)[1] == {'add': 1, 'mul': 0, 'div': 6}
    assert user2_functions(add, 1, 2)[1] == {'add': 2, 'mul': 0, 'div': 6}
    assert user2_functions(add, 1, 2)[1] == {'add': 3, 'mul': 0, 'div': 6}
    assert user2_functions(add, 1, 2)[1] == {'add': 4, 'mul': 0, 'div': 6}
    assert user2_functions(mul, 1, 2)[1] == {'add': 4, 'mul': 1, 'div': 6}
    assert user2_functions(add, 1, 2)[1] == {'add': 5, 'mul': 1, 'div': 6}
    assert user2_functions(div, 1, 2)[1] == {'add': 5, 'mul': 1, 'div': 7}
    assert user2_functions(mul, 1, 2)[1] == {'add': 5, 'mul': 2, 'div': 7}
    assert user2_functions(print, 'None')[1] == {'add': 5, 'mul': 2, 'div': 7}
