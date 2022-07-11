#Lets work with dictionary, instead of tuples

def mean(*args): #Tuple
    return sum(args)/len(args)

def users(**kwargs): #Dictionary
    print(kwargs, type(kwargs))

users(m_=[10,9,8],n_=[7,6,6])

def conv(*args,**kwargs):
    print(args,kwargs)

conv(1,2,3,4,5, m=[True],n=[False])
