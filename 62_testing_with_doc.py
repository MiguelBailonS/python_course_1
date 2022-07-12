#How to test our function?
#We will use the docstrings & a command in console known as doctest.

#We use '>>>' as a console cmd
#In the next line, we write the value that it is going to be returned

def add(n_1,n_2):
    """
    *Add a brief description of the function:
    -> The function return the sum of two int numbers.
    *Arguments:
    Arguments:
        n_1 (int)
        n_2 (int)
    It returns the sum of the parameters.

    TODO:
        * 

    >>> add(10,20)
    30

    >>> add(100,10)
    110

    """
    return n_1 + n_2
#We can use the following command in console to test docstring 
# python -m doctest 62_testing_with_doc.py 

#Let test another function

def test2(n_1,n_2):
    """
    >>> test2(10,20)
    -10
    >>> test2(10,21)
    10
    """
    return n_1 - n_2

#When executing the next test, we'll obtain one failed test.