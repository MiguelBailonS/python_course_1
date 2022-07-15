class Circle:
    pi = 3.141592


    #To convert it to a class method, we'll use decorators.
    #The class' methods can access to the class' atributtes through the parameter cls.
    @classmethod
    def area(cls,radio): #As this is a Class Method, it will use a parameter called cls
        return cls.pi * (radio**2) #CLS is a convention.

area = Circle.area(2) #We are using the class method directly in this line without creating an object of the class.
print(f'Area of the circle: {area}')