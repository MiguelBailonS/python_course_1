name = "Jose"
last_name = "Bailon"

#Prrint the values directly in console
#Print can be used to print n values. e.g.

print(name, last_name, "Silva")

#You can print any value type or Objects: Int, Bool, String, Tuple, List, etc
#The print function add per default a blank space between parameters
print(name, last_name, "Silva", 1)

print(name, last_name, "Silva", 1.1)

print(name, last_name, "Silva", [10,20,30])

print(name, last_name, "Silva", (10,20,30))

#You cant manage the separator when printing with param "sep=''"

print(name, last_name, "Silva",sep = '-')
print(name, last_name, "Silva",sep = '@')
print(name, last_name, "Silva",sep = '=')

#The function print doest not generate a new type.