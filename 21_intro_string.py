languages = 'Python Ruby Java Rust C++ C'

#Eliminate blank spaces and create a list.
list_languages = languages.split()
print(list_languages)

#Lest see how it works with another 'symbol' or separator
languages = 'Python-Ruby-Java-Rust-C++-C'
list_languages = languages.split('-')
print(list_languages)


#Lets try with another complex separators

languages = 'Python/-/*Ruby/-/*Java/-/*Rust/-/*C++/-/*C'
list_languages = languages.split('/-/*')
print(list_languages)

#Now, les get another list with the elements we desired or ocurrences of the argument

languages = 'Python/-/*Ruby/-/*Java/-/*Rust/-/*C++/-/*C'
list_languages = languages.split('/-/*',3)
print(list_languages)


#Now lets see 'Join' function

language = ['Python','Ruby','Java','Rust']
#Lets generate from language list a String

#It will use the characters inside ' ' to join the elements from the list
str_languages = ' '.join(language)
print(str_languages)

#It will use the characters inside '-' to join the elements from the list
str_languages = '-'.join(language)
print(str_languages)

#The method/function split returns a list
#The method/functions join return a string