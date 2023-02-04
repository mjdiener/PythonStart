# this is my scratch file for learning Python
# Learning from:  https://www.learnpython.org/
# Matthew Diener 
#new line


# __________________BASIC START _____________________________________
from ast import Import


print("try again")
x=5
if x==1:
        print("x is 1 ")
        print("just adding text")
if x!=1: print(x)


# _______________________NUMBERS _______________________________________
myint=80
print(myint)
myfloat=7.6677
print(myfloat)
myfloat=int(7)
print (myfloat)
a,b=3,4  #can assign on sameline
print(a,b)
print("format number %.1f" % myfloat)   #use %.NUMBERf to limit number of decimals displayed - ONLY 0s???
print("hex numer"+ hex(myint))    #display hex version of number


# ___________________STRINGS - use double quote if string contains apostrophe______________________
mystring='Hello'
print(mystring)
mystring="Hello"
print(mystring, len(mystring))  #use LEN for length of a string also
print(mystring + ' world' )
print(mystring + str(a))  #str to convert to a string
print(mystring.index("o"))  #find letter position ina string, remember 1st char is position 0
print(mystring.count("l"))   # count the number of a certain string within a string
print(mystring[1:3])       # print a subset of string
print(mystring[::-1])   # reverse a string
print(mystring.upper())   #capitalize a string
print(mystring.lower())   #makes a string lower case

mystring = 'Saturday'
myfloat = 3.14
myint = 42

# testing code
speed= "fast"
if mystring == "Saturday":
    print("String: %s" % mystring)  # %s substitutes a string, can be several
    print("example: %s %s "%(mystring,speed) )  # using two substituteted strings
if isinstance(myfloat, float) and myfloat == 3.14:
    print("Float: %f" % myfloat)   #can substitute floating with %f
if isinstance(myint, int) and myint == 42:
    print("Integer: %d %d" %(myint, a))  # can substitute decimals with %d
if isinstance(myint, int) and myint == 42:
    print("Integer: {} {}".format(myint, mystring))  # can also use .FORMAT {} to cover all scenarios


# ________________________LISTS ____________________________________________
mylist=[]
mylist.append(1)
mylist.append(2)
mc=mylist.count(2)  #count the number of 2's
print (mylist,mc)
mylistb=[1,2,17]
print (mylistb[2])  #list ranges start at 0, so a 3 item list is position 0,1,2
myliststring= []
myliststring.append("first")
myliststring.append("  second")
print(myliststring, len(myliststring))   
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers  # can concatenae two lists together
print(all_numbers,len(all_numbers))   #use LEN for length of an array
findme = 2
if findme in mylistb:    # use "in" to find value in a list
    print ("true")


#___________________ BASIC OPERATORS __________________________________________
number = 1+2*3/4.0  # usual math symbols
print(number)
remainder = 11 %3  # use % for remainder
print (remainder)
squared = 7**2     # ** for power
cubed=5**3
print(squared,cubed)
try2 = "h" * 5    #can also repeat strings with * symbol and number
print (try2)
print([1,2,3] *4)   # can also repeat lists with * and number


#________________________ STRING FORMATTING_______________________________
name="Matt"
age=23
print("Hello, %s!" % name)
print("Hello, {}! age {}" .format(name,age))


#____________________________CONDITIONS _________________________________________
# = is assignment
# == are they equal?
# can also use "is" instead of ==
# != are they NOT equal?
# "and" and "or" are valid
# "not" inverts an expression


# ________________________IF STATEMENT_______________________________________
statement = False
another_statement = True
if statement is True:
    print ("true")  # do something
    pass
elif another_statement is True: # else if
    print ("elif true")  # do something else
    pass
else:
    print ("else true")   # do another thing
    pass


# __________________________________FOR LOOP ___________________________________
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)
# Prints out 3,4,5
for x in range(3, 6):
    print(x)
# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
print("_____________________")


# _______________________________WHILE LOOP _________________________________________
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1


# __________________________________BREAK and #CONTINUE _______________________________________
#break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, 
# and return to the "for" or "while" statement. A few examples:
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue  # if x is even then continue loop, do not perform print step
    print(x)


#_________________________________________FUNCTIONS _____________________________________________________
def my_function():
    print("function working")

def my_function_with_args(username, greeting):   #pass values to a function
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):  # RETURN a value to calling line
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print(x)
print(sum_two_numbers(5,6))


# ____________________________________CLASSES AND OBJECTS______________________________________________
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

print(myobjectx.variable)   #access variable within an object instanced within a class
myobjectx.function()        #execute a function from within an object instanced froma class 
print(myobjecty.variable)

# _INIT_() FUNCTION - CALLED WHEN THE CLASS IS BEING INITIATED.  uSED FOR ASSIGNING VALUES IN CLASS
class NumberHolder:
   def __init__(self, number):   # SELF represents the instance of a class 
       self.number = number    # binds the attribute with the given argument
   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'

# A Sample class with init method
class Person:
     # init method or constructor
    def __init__(self, name):
        self.name = name
     # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
  
# Creating different objects
p1 = Person('Nikhil')
p2 = Person('Abhinav')
p3 = Person('Anshul')
 
p1.say_hi()
p2.say_hi()
p3.say_hi()


#______________________________________________ INIT WITH INHERITANCE _____________________________________________
class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something
 
class B(A):    # THIS MEANS THAT CLASS B INHERITS ALL THE ATTRIBUTES FROM CLASS A, B IS A CHILD CLASS OF A
    # COULD ALSO INHERIT FROM TWO CLASSES - cLASS C(A, B) = CLASS C INHERITS FROM BOTH A AND B
    def __init__(self, somethingb):
        # Calling init of parent class
        A.__init__(self, somethingb)
        print("B init called")
        self.somethingb = somethingb
  
obj = B("SOMEthing")

# EXERCISE
# We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible 
# worth $60,000.00 with a name of Fer. And car2 to be a blue van named Jump worth $10,000.00.
class vehicle:
    def __init__(self,name, color, style, worth): 
        self.color=color
        self.style=style
        self.worth=worth
        self.name=name
    def say_info(self):
        print("this vehicle {} is a {} {} worth ${}" .format(self.name,self.color,self.style,self.worth))

car1 = vehicle('Fer','red','convertible',60000)  #numbers are passed without quotes, else they are strings
car2 = vehicle("Jump","blue","van",10000)

car1.say_info()    #call a function within object
car2.say_info()
print(car2.name,car2.color,car2.style,car2.worth)  #can also directly access object 


#___________________________________________DICTIONARIES__________________________________________________
#  A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. Each value 
# stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, 
# a list, etc.) instead of using its index to address it.
phonebook = {}   #OR phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
print(phonebook["John"])
del phonebook["John"]
for name  in phonebook.items():  #Iterate through a dictionary
    print("Phone number of %s is %d" % (name, number))
 

#________________________________MODULES AND PACKAGES _________________________________________
#import draw  # ERRORS WITH IMPORT! - COME BACK AND FIX  https://www.learnpython.org/en/Modules_and_Packages
import sys
sys.path
#imports from file named draw.py

def play_game():
    b=17

def main():
    result=play_game()
   #draw.draw_game(result)

 # this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()


# ___________________________ NUMPY ARRAYS ____________________________________________
# Numpy arrays are great alternatives to Python Lists. Some of the key advantages of Numpy arrays are that they are fast, easy to work with,
#  and give users the opportunity to perform calculations across entire arrays.
# In the following example, you will first create two Python lists. Then, you will import the numpy package and create numpy arrays out of 
# the newly created lists.
# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

 # Import the numpy package as np
""" import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)
print(type(np_height))
print(np_height)
print(np_weight)  """

#  now at https://www.learnpython.org/en/Numpy_Arrays
