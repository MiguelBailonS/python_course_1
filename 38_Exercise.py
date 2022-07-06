#The reading is from left to right
#Thourgh the Logical Operator we can assign values to the variables.
#The first variable to be True is the one that is going to be stored.
variable = 'Cody' or 'Codigo Falicito'
print(variable)

#If we compare with an empty string or False, the variable
#is going to stored the first true value he found.

variable = '' or 'Codigo Facilito'
print(variable)

#We are not limited to work with strings.
#We can work with all the other types of variables we have seen.

variable = '' or 0 or 0.0 or [] or () or True
print(variable)

#It is usefull to assign values to variables when we need to assign it when a condition is necessary.

list = []
name = 'Miguel'

if list: #False
    var = list
else:
    var = name
print(var)
#Another way to do it
var = list or name
print(var)


list = [1]
var = list or name
print(var)
