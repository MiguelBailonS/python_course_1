def mean_ref(*args): #We are saying that all the assigned elements will be assigned to a tuple
    return sum(args)/len(args)

def conv(p1,p2,p3):
    print(p1,p2,p3)

conv(1,2,3)

#Python assigned correctly the arguments to the parameters
def conv(p1,p2,*args):
    print(p1,p2,args)
conv(1,2,3,4,5,6 )

def conv(p1,p2,*args,p4=2):
    print(p1,p2,args,p4)

conv(1,2,3,4,5,6)

#What happen if I want to assign a value to p4?
#We can do the following, using the names

conv(1,2,3,4,5,6,p4=7)
#When our program has two o more functions, we add two lines between functions.