#Docstring
#How to create documentation for Python

#The attribute doc allows us to 

#__doc__ 

#In Python exists Objets that can be documented with the attribute __doc__ (Modules, Classes, Methods & Functions)
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
    """
    return n_1 + n_2

print(add.__doc__) #We can visualize the documentation of the function.
#The Docstring its being store in the attribute __doc__

#We can obtain the same result with help

help(add)
#or
print(help(add))