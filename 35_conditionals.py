#Lets see how "If statement works"
result = 10
comparison = result > 10
"""
E.g.
    if(Statement to evaluate):
    ....print("Statement true")
    ^
    |- This four spaces or ident is necessary.
"""

if (comparison):
    print("Statement: True")


result = 11
comparison = result > 10
if(comparison):
    print("Statement: True")

#Another way to use If statements (more recomendded)

if(result> 10):
    print("Statement: True")

#Using Logical Operators

if( result > 10 and result < 20):
    print("Statement: True")

#If the statement is not true, we can use "else" case to execute if the statement its not true
#The use of the block "else" it is optional.

if (result > 100):
    print("Statement: True")
else:
    print("Statement: False") 