msg = 'This is a message'

#Lets see the methods of alignment/justification
"""
The are three methods
    - ljust -> Justify to the left
    - rjust -> Justify to the right
    - center ->Center

This functions doesnt modificate the string. Remember, the Strings are not mutable.

"""
align_msg = msg.ljust(20)
print(align_msg, '.')

align_msg = msg.rjust(20)
print('.', align_msg, '.')

align_msg = msg.center(20) 
print('.', align_msg, '.')

#These three methos recieve as arguments the quantity of blank spaces to add to the string.
