#What happen if our decorate function receive arguments
# and return a value

#Lets modify our decorator 
def func_a(func_b):
    def func_c(*args,**kwargs):
        res = func_b(*args,**kwargs) 
        return res
    return func_c


@func_a 
def add(x_,y_):
    return x_ + y_

res = add(10,20)
#print(res) #Why we are obtaining None?
#It is because function C doesnt return any value

#Lets refactor func_a
print(res) #Now we obtained the result

#The decorator should be very flexible to accept any qty of arguments.
#This is the basic structure for the decorator function