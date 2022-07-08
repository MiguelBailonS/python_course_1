#Lets refactor the code of class 43

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


addition(x_,y_)