#Lets introduce the while loop to execute n times a code until a condition is reached.

counter = 1

while counter <= 10:
    print(counter)
    counter = counter + 1

number = 4321
counter_digits = 0
print("-------------------------")

while number >= 1:
    counter_digits = counter_digits + 1
    number = number / 10
print(counter_digits)

number = 987654321
counter_digits = 0
print("-------------------------")
while number >= 1:
    counter_digits = counter_digits + 1
    number = number / 10
print(counter_digits)

#Another way to increase values
print("-------------------------")

number = 987654321
counter_digits = 0
print("-------------------------")
while number >= 1:
    counter_digits +=  1
    number = number / 10
print(counter_digits)

#With the cycle while we can use a "Else"

number = 987654321
counter_digits = 0

while number >= 1:
    counter_digits = counter_digits + 1
    number = number / 10
else:
    print("While end.")
print(counter_digits)


number = 987654321
counter_digits = 0

while number >= 1:
    counter_digits = counter_digits + 1
    number = number / 10
else:
    print(counter_digits)

