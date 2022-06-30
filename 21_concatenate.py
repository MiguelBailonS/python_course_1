#The Strings in Python are not mutable.

Name = 'Miguel Alejandro'
Last_name = 'Bailon Silva'

#Create a new variable to create the full name

#Concatenate this two variables: Name + Last_name
full_name = Name + Last_name
print(full_name)

#To fix this problem: Miguel AlejandroBailon Silva, lets add a new space
full_name = Name +  ' ' + Last_name
print(full_name)

full_name = Name +  ' ' + Last_name + '.'
print(full_name)

full_name = 'Mr. '+ Name +  ' ' + Last_name + '.'
print(full_name)

#Lets see another way we can concatenate Strings
#Formatted output
full_name = 'Mr. %s %s.' %(Name, Last_name)
print(full_name)

#New formatted output
#%s replace the values of the strings that are inside the parenthesis
full_name = 'Mr. %s %s %s.' %(Name, Last_name, 'Tired')
print(full_name)

