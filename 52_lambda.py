#A function lambda, aka anonymous function, it is only expressed in a single line of code
#Generally, this function has no name

#Refactor of class 51

#Name of function lambda = lambda (parameter1,parameter2,parameter3, ...) : body of the function
C_to_F = lambda grade : grade*1.8+32
#The function lambda will return the result of the function's body
print(C_to_F(1),C_to_F(-1))


#It is obligatory to write the function's body.
#Even if it doesnt return a value
'''
    sample = lambda : True
    sample = lambda p1=10,p2=20,p3=30: p1+p2+p32
    sample = lambda *args, **kwargs: len(args) + len(kwargs)
'''

