#Which is the advantage to use generators.
#The advantage is the way we iterate the function.

#Another advantage, is the memory use. 
#When we are working with large set of data. Reserving more memory and only using it when it is necessary.

def even():
    for number in range(0,20,2):
        yield number

generator = even()

print(next(generator)) #res-> 0 #Obtain elements on demand
print(next(generator)) #res-> 2
print(next(generator)) #res-> 4

#We are going to work with error. (Exception Error)

while True:
    try:
        value = next(generator)
        print(value)
    except StopIteration:
        print("Generator has stop.")
        break; #Remember to add the break. Otherwise, it will continue to print 'Generator has stop.' indefinetely
    