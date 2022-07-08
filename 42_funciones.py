#Lets see how to create functions

#We have to define first the use of the reserved word def
#You can create the name of the function following the snake case nomenclature

# def function_name(parameters)
# def function_name() <- without parameters

def addition():
    x_ = int(input('First number: '))
    y_ = int(input('Second number: '))

    result = x_ + y_
    print(result)

addition() #Adittion function does not require any parameter

#Inside fucntions, we can call another functions.

#You can call it anytimes you want.

addition()

#Atomic functions