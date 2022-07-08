course = 'Python course'


print('First case...\n')

#We will print each character 
for character in course:
    print(character)


print('Second case...\n')
for character in course:
    if character == 'c':
        #Break allow us to finalize the cycle for. Or while
        break;
    print(character)
#Using break, we can interrupt any cycle like for and while.

#Now lets see what continue do

#The word "continue" will make that the cycle continue to the next iteration

print('Third case...\n')
for character in course:
    if character == ' ':
        continue
    print(character)

