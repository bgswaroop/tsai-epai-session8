def q1_check_doc_str_length():
    """
    Global Function
    Task: Write a closure that takes a function and then check whether the function passed has a docstring with more
    than 50 characters. 50 is stored as a free variable.
    print - "Valid Docstring" when condition is satisfied and "Invalid Docstring" otherwise
    :param func: Any function
    :return: local function check_doc_str_length
    """

    doc_str_length = 0

    def check_doc_str_length(func: 'any function') -> bool:
        """
        Local Function
        Check length of doc string
        :param func: Any function
        :return: bool
        """
        nonlocal doc_str_length
        if func.__doc__:
            doc_str_length = len(func.__doc__)
        else:
            doc_str_length = 0

        print(func)
        if doc_str_length > 50:
            print('Doc string has more than 50 characters')
            return True
        else:
            print('Doc string has less than 50 characters')
            return False

    return check_doc_str_length


def q2_get_next_fib_number():
    """
    Global Function
    Task: Write a closure that gives you the next Fibonacci number
    :return: local function generate_fib_sequence
    """

    fib_n1 = 0
    fib_n2 = 1

    def generate_fib_sequence():
        """
        Local Function: Generates fib sequence
        :return: next fib number based on the previous two (non-local) free variables
        """
        nonlocal fib_n1
        nonlocal fib_n2
        next_fib = fib_n1 + fib_n2
        fib_n1 = fib_n2
        fib_n2 = next_fib
        return next_fib

    return generate_fib_sequence


def add(a, b):
    """
    Generic method to add two objects, on which + is defined
    :param a: object 1
    :param b: object 2
    :return: the sum of a and b
    """
    return a + b


def mul(a, b):
    """
    Generic method to multiply two objects, on which * is defined
    :param a: object 1
    :param b: object 2
    :return: the product of a and b
    """
    return a * b


def div(a, b):
    """
    Generic method to divide two objects, on which / is defined
    :param a: object 1
    :param b: object 2
    :return: the div of a and b
    """
    return a / b


def q3_update_local_counts():
    """
    Task: Write a closure that can keep a track of how many times add/mul/div functions were called, and update a
    global dictionary variable with the counts
    :return: local function count
    """
    count_dict = {'add': 0, 'mul': 0, 'div': 0}

    def count(func, *args, **kwargs):
        """
        Call any function
        :param func: function name
        :param args: positional arguments of func
        :param kwargs: keyword arguments of func
        :return: function result, dictionary of counts
        """
        nonlocal count_dict
        if func.__name__ in count_dict:
            count_dict[func.__name__] += 1
        return func(*args, **kwargs), count_dict
    return count


def q4_update_counts_global(count_dict=None):
    """
    Task: Modify above such that now we can pass in different dictionary variables to update different dictionaries
    :return: local function count
    """
    if not count_dict:
        count_dict = {'add': 0, 'mul': 0, 'div': 0}

    def count(func, *args, **kwargs):
        """
        Call any function
        :param func: function name
        :param args: positional arguments of func
        :param kwargs: keyword arguments of func
        :return: function result, dictionary of counts
        """
        nonlocal count_dict
        if func.__name__ in count_dict:
            count_dict[func.__name__] += 1
        return func(*args, **kwargs), count_dict

    return count