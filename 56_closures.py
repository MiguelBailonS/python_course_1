#Closures
#A closure is a function that can generate dynamically another function.
# This function can access to the local variables even if the function is terminated.

def greetings(user): #This function is a closure
    msg = f'Welcome! {user}.' #Local Variable

    def show_msg():
        print(msg)
    
    return show_msg

user = 'Miguel'
resp_f = greetings(user) #Returning nest function show_msg

#Msg is a local variable inside greetings function and it is destroyed after calling greetings()
#Nevetheless, when executing show_msg, it is going to print the value of msg
#This means, that in some way, it has 'memory'.
#Even if we try to change the value of user
resp_f() # Executing nest function show_msg
user = 'Alejandro'
resp_f() # Executing nest function show_msg