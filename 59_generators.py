#A generator is a special type of function which return objects that we can iterate 
# without the termination of the function.

def even(): #This is not a generator 
    for number in range(0,100,2):
        print(number)

def even_2():
    for number in range(0,100,2):
        return number

def even_3(): #This is a generator function -> Lazy iterator
    for number in range(0,100,2):
        yield number #With yield, the function is 'paused', until it is called again.

#even()

print(even_2()) #

print(even_3())#We obtain an generator object type

for even in even_3(): #Now we are iterating a generator function
    print(even)
