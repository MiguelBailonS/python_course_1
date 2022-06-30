numbers  = (2,4,6,8)
#This is a better way
two,four,six,eigth = numbers

print(two)
print(four)
print(six)
print(eigth)

#Optinal form

two = numbers[0]
four = numbers[1]
six = numbers[2]
eigth = numbers[3]

print(two)
print(four)
print(six)
print(eigth)
#Increease numbers of elements
numbers  = (2,4,6,8,10)
#This is a better way
#Obtain an error because there is too much elements to unpack

#two,four,six,eigth = numbers

#To improve this, we use the following assigment

#The symbol '*' represent lists
two, four, six, eigth, *omitted_values = numbers
print(two)
print(four)
print(six)
print(eigth)
print(omitted_values)

#Ignore the created variable
#In order to ignore values, we can use the symbol '_'
#This means that the other elements are going to be ommited
two, four, six, eigth, *_ = numbers
print(two)
print(four)
print(six)
print(eigth)


#If we want to ignore the elemens after index 4, but want to obtain the last two index
numbers  = (2,4,6,8,10,10.5,11,12,14)
two, four, six, eigth, *_ , twelve,fourteen= numbers
print(two)
print(four)
print(six)
print(eigth)
print(_)

#Lets do the following execise: Ignore 3,8,10.5,12

numbers  = (2,4,6,8,10,10.5,11,12,14)
two, _, six, eigth, *_ , twelve,fourteen= numbers
print(two)
#print(four)
print(six)
print(eigth)
print(_)

#To indicate a Python that we want to create a list from ignored elements, we use the '*' symbol.



