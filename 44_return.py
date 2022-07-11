#Lets refactor the code of class 43
#Lets use the reserved word 'return' to obatin a value
# Lets work with this return value.


def addition(x,y):
    result = x + y
    return result

def adittion_ref(x,y):
    return x+y

#This function return a tuple with two values
def adittion_ref_two(x,y):
    return x+y, 'Another value to return' #It is not recommended to return more than 3 values

x_ = int(input('First number: '))
y_ = int(input('Second number: '))

addition(x_,y_)
#Now, we can store the value inside a new variable
res = addition(x_,y_)
print(res)

#Lets see this refactor
res = adittion_ref(x_,y_)
print(res)

#Lest see this refactor to obatin two values
#Obtain the values unziping the tuples.
res, msg = adittion_ref_two(x_,y_)
print(res)
print(msg)

#If we want to omit the second value:
res, _ = adittion_ref_two(x_,y_)
print(res)
