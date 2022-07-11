#A decorator is a function that its input is a function
#Its output is another function

'''
func_a = Main func (decorator)
func_b = Function to decorate (argument) ((input))
func_c = Function decorated (return) ((output))

func_a(func_b) -> func_c
'''

def func_a(func_b):
    def func_c():
        #We are extending the functionalities.
        print('Before call')
        func_b() #Calling greetings
        print('After call1')
        #print('Decorated func!')
        pass
    return func_c


@func_a #In order to decorate/extend functionality. We have to use the next assigment
#In this way, we are saying that greetings functions is being decorated. (func_b)
def greetings():
    print('Welcome!')

greetings() #We are not executing greetings, but func_c.


#In order to execute greetings..., let refactor func_a
#Exists decorators for classes, methods, etc.