#Create a range to create a sequence of int numbers that we can iterate

#range() will start at 0
#range will omit the value of the argument
range_ = range(11)

#range_ will have from 0 to 10.

print(range_)

for value in range_:
    print(value)

#If we can iterate from a value from 0 to 20, we can do the following
range_ = range(21)
for value in range_:
    print(value)


#Another way to iterate
for value in range(21):
    print("3rd way",value)

#We can start from another value

for value in range(3,9):
    print("Start different",value)

#Lets see the skips

for value in range(3,9,2):
    print("Steps between values",value)


"""
Now lets see numbers
"""

numbers = [10,15,20,25,30,35]

#the function enumberate will return a tuple with two values
#The first, index, and then, the number corresponding to the index
#Enumerate return an iterable object
for index,number in enumerate(numbers):
    print(index,number)

#In the left side index
#In the right side number

#Just to know, you can change the index using the second parameter
for index,number in enumerate(numbers,10):
    print(index,number)