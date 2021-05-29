# Multi threading example in python
# defining class
# Importing library for threading 
from threading import *
class mgk(Thread): # passing the threading to the class
# defining a method
    def run(self):
       for i in range(5):
          print ("Hello Gokul")

class king(Thread): #passing the threading to the class
# defining a method
    def run2(self):
       for i in range(55):
        print ("Hi kumar")

# Creating the objects 
g1 = mgk() # object 1 is created
g2 = king() # object 2 is created

# calling the methods
 # We need to use start instead of the method name because in threading library the start is defined 
g1.start()
g2.start() 