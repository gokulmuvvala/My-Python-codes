# Working with constructor in inheritance
# defining classes
class A: #(parent class)
    # Own constructor (or) own init method 
    def __init__(self):
        print("in A init")
    def feature1(self): 
        print("feature1 is updated")
    
    def feature2(self):
        print("feature2 is updated")

class B(A): #(child class)
    # Own constructor (or) own init method 
    def __init__(self):
        super().__init__() # Trying to call the init of super class (A)
        print("in B init")
    def feature3(self):
        print("feature3 is updated")
    
    def feature4(self):
        print("feature4 is updated")


# creating the objects 
a1 = B()




    

