def greetings():

    def msg():
        print('Welcome!')

    return msg

resp_f = greetings() #Returning the nest functions msg()
print(resp_f,type(resp_f))

resp_f() #Executing the nest function msg()