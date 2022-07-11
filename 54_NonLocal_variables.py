#Closure
# You have to use the concepts of Scope & Nested Functions
# Lets first see: Non local variables

letter_d = 'd'
def main_f():
    letter_a = 'a' #Local Variable
    letter_b = 'b'

    def nest_f():
        letter_c = 'c' #Local Varible
        #letter_b = 'e' #The value for the upper variable is not changed. 
        nonlocal letter_b  #With non local name, it will find the variable letter_b in upper levels
        letter_b = 'e' #Changing the value of the upper variable letter_b from b to e
        print(letter_a,letter_b, id(letter_b)) 
        print(letter_d)


    nest_f()
    print(letter_b,id(letter_b))
    #print(letter_c)
    '''
    Traceback (most recent call last):
    File  line 15, in <module>   main_f()
    File  line 13, in main_f     print(letter_c)
    NameError: name 'letter_c' is not defined
    
    This error occurs due to the scope of the function.
    Letter C cannot be seen outside nest_f function.
    Instead, the scope of letter_a and letter_b variables are an upper level than nest_f
    Therefore, nest_f can see those variables.
    '''

main_f()