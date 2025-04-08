# Class declaration
class Human:
    #Creating Docstring for Class
    ''' 
    This is human class..!!
    Hello and Bye
    '''
    def __init__(self,age,name): #Initialization of class
        self._a = age
        self._n = name
    
    def __str__(s):  # String representation of class 
        return f'I am {s._n} and {s._a} age older'
    
    def walk(s):
        if(s._a >= 5):
            print("I can run")
        else:
            print("I can crawl")


# Object Creation
h1 = Human(12,"Logesh")
h2 = Human(name = "Rajiv", age = 29)
h3 = Human(2,"Baby")
print(h1,'\n',h2)
h1.walk()
h2.walk()
h3.walk()
print(h1._n,h1._a)
print(h2._n,h2._a)
print(h3._n,h3._a)

# Docstring
#print(help(list)) #Returns Docstring of inbuilt Function
def add(a,b):
    return a+b
print(help(add))
def subtract(a,b):
    '''
    A method to subtract to integers
    a: Number
    b: Number
    ....
    '''
    return a-b
print(help(subtract))
#Print Docstring for class Human
print(help(Human))

    