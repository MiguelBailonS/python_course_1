#We can create functions that can receive any quantity of arguments
#For example: print function

print('String', True, 1,1.56)

#Lets create a function to calculate the mean

#Sum will return the total value of the elements inside list
def mean(list): #1 parameter listed
    return sum(list) / len(list)

mean_ = mean([10,4,2,10,5]) #1 parameter given
print(mean_)

#What happen if I direcly five elements inside the function.

def mean_ref(*list): #We are saying that all the assigned elements will be assigned to a tuple
    print(list)
    print(type(list))
    return sum(list)/len(list)

mean_ = mean_ref(10,4,2,10,5)
print(mean_)

#For convention: All parameters that has the symbol '*' must be called as args\
def mean_ref(*args): #We are saying that all the assigned elements will be assigned to a tuple
    return sum(args)/len(args)

mean_ = mean_ref(10,4,2,10,5)
print(mean_)