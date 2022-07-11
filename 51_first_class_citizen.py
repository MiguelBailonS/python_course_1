#Demonstration in Python of First Class Citizen for Functions
# Functions can be assigned to variables
# Functions can return function
# Functions can be arguments for another functions

def C_to_F(temp):
    return temp*1.8+32

print(C_to_F(10), C_to_F(1), C_to_F(-1))

ptr_func = C_to_F #Calling a function trough a variable #Avoid writing the parenthesis
print(type(ptr_func)) #Function class

print(ptr_func(10))