def oper():
    def deposit(amount, balance):
        return amount + balance
    
    def retire(amount, balance):
        if(amount <= balance):
            return balance - amount
        else:   
            return None

    print(deposit(10,20))   #30
    print(retire(50,10))    #None
    print(retire(50,70))    #20


oper()

#We can have functions with n levels
#For convention, a two level functions is enough and legigle for reading.
def oper_2(amount,balance,type = 'deposit'):
    def deposit(amount, balance):
        return amount + balance
    
    def retire(amount, balance):
        if(amount <= balance):
            return balance - amount
        else:   
            return None

    if(type == 'deposit'):
        print(deposit(amount,balance))
    elif (type == 'retire'):
        print(retire(amount,balance))
print('----oper2----')
oper_2(10,20)               #30
oper_2(10,30,'retire')      #20
oper_2(30,10,'retire')      #None