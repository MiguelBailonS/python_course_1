#Lets talk about callbacks
#Functions that are passed to another function as an argument

mean_f = lambda *args : sum(args)/len(args) #Tuple
print(mean_f(10,20,32))

pass_f = lambda score : (score >= 7)
print(pass_f(5),pass_f(7))

def pass_class(mean_f, pass_f, *args):
    mean_= mean_f(*args) #Passing all n arguments to the function mean_f
    if(pass_f(mean_) == True):
        print(f'Pass {mean_}.')
    else:
        print('Fail')

pass_class(mean_f,pass_f,5,7,9,10)
#Callbacks are very usefull in modular programs.
#We can create another function to determine if a student pass its class depending on assistans

assistance_f = lambda assistant: assistant >= 50

pass_class(mean_f,assistance_f,5,10,5) #Fail
#Now the student doest pass because assitant 

#We can change again the function.
#You can do this because the modularity of the function we create
pass_class(mean_f,pass_f,9,9,9) #Pass