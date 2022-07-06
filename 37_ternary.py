#If the student obtain a grade equal or greater than 7, it is going to set the color of a LED to be green.
# In another case, the color of the LED will be red.

grade = 10
LED = None

if grade >= 7:
    LED = 'Green'
else:
    LED = 'Red'

print("Your color is",LED)

#Use of Ternary
#When the conditionals are in one line of code, the else statement MUST be in the line.
grade = 5
LED = 'Green' if grade >= 7 else 'Rojo'
print("Your color is",LED)