#Lets see the case "elif"

grade = 8

if(grade == 10):
    print('AP')
else:
    print('RP')

#Lets add a new case to evaluate the grade you obtained

if(grade == 10):
    print('AP Yei')
elif(grade == 8 or grade == 9):
    print('AP')
else:
    print('RP')

grade = 7

#The way the statements are evaluated are from top to bottom, and if any case is true
#the block of conditions are stop and enter in the case that the statement it is true.
#If none statement is true, then, the "else" case is executed.
if(grade == 10):
    print('AP Yei')
elif(grade == 8 or grade == 9):
    print('AP')
elif(grade == 7 or grade == 6):
    print('AP...')
else:
    print('RP')
