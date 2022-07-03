phrase = "This was not real for me, neither for you"

#Lets find how many times 'neither' appear on phrase

counter = phrase.count('neither')
print(counter)

#Lets see another examen

phrase = "This was not real for me, neither for you, neither for them."
counter = phrase.count('neither')
print(counter)

#Lets see how many times the letter 'e' appears

phrase = "This was not real for me, neither for you, neither for them."
counter = phrase.count('e')
print(counter)

#What happen if the string doesn't exist?
phrase = "This was not real for me, neither for you, neither for them."
counter = phrase.count('0')
print(counter)

#Lets see for Bool values to know when the string exists or no in the string.

phrase = "This was not real for me, neither for you, neither for them."
existString = "neither" in phrase
print(existString)

#What happen if we write in on Capital Letters


phrase = "This was not real for me, neither for you, neither for them."
existString = " NEITHER" in phrase
print(existString)

#Lets standarize the phrase to Capital Letters\


phrase = "This was not real for me, neither for you, neither for them."
existString = "NEITHER" in phrase.upper()
print(existString)

#We can negate the declartions


phrase = "This was not real for me, neither for you, neither for them."
existString = "NEITHER" not in phrase.upper()
print(existString)

#TODO We can check if the String ends or starts with another string

#Use of startswith() function
phrase = "This was not real for me, neither for you, neither for them."
startsWith = phrase.startswith('This')
print(startsWith)

phrase = "This was not real for me, neither for you, neither for them."
startsWith = phrase.startswith('T')
print(startsWith)

phrase = "This was not real for me, neither for you, neither for them."
startsWith = phrase.startswith('C+')
print(startsWith)

#Use of endswith() function

phrase = "This was not real for me, neither for you, neither for them."
startsWith = phrase.endswith('.')
print(startsWith)

phrase = "This was not real for me, neither for you, neither for them."
startsWith = phrase.endswith('Hello')
print(startsWith)
