#Lets refactor the code of class 42

def addition(x,y):
    #The variables x,y will only exists inside the function addition(x,y)
    result = x + y
    print(result)

x_ = int(input('First number: '))
y_ = int(input('Second number: '))

#Lets see this error
#addition()
"""
Traceback (most recent call last):
  File line 11, in <module>
    addition()
TypeError: addition() missing 2 required positional arguments: 'x' and 'y'

"""
#The arguments are assigned accordint to its positions.

addition(x_,y_)