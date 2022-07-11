#We can define parameters that are optional

def area_circle(r, pi):
    return pi* (r**2)
#Set a default value to pi.
#Now, the parameter pi is optional
#We establish default value reading from rigth to left

def area_circle_ref(r,pi=3.14):
    return pi* (r**2)

#Parameter with default values always have to be in the rigth side
#This is an error
# def area_circle_ref(pi=3.14,pi):

res = area_circle(1,3.14)
print(res)

#If a parameter it is ommited, we get an error
#res = area_circle(1)
#print(res)
'''
Traceback (most recent call last):
  File , line 13, in <module>   
    res = area_circle(1)
TypeError: area_circle() missing 1 required positional argument: 'pi'
'''
print('Example 2 ----\n')
res = area_circle_ref(1)
print(res)

#if we want to use the default value, then we can rewrite it.
res = area_circle_ref(1,3.1415)
print(res)

#We can assign the names of the parameter when invoking the function
res = area_circle_ref(r = 1 , pi = 3.1415)
print(res) #Same result
res = area_circle_ref(pi=3.1415, r = 1)
print(res) #Same result
#If we write a parameters' name that doesnt exist will generate an error