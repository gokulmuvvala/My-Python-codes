# multiply inheritance 
# defining classes
class A: #(parent class)
    def __init__(self):    # Own constructor (or) own init method 
        print("in A init")
    def feature1(self): 
        print("feature 1-A is updated")
    
    def feature2(self):
        print("feature2 is updated")

class B: #(parent class)
     def __init__(self):     # Own constructor (or) own init method 
         print("in B init")
     def feature3(self):
        print("feature 1-B is updated")
    
     def feature4(self):
        print("feature4 is updated")
# class C is child of A,B  
class C(A,B): #(child class)
    def __init__(self):    # Own constructor (or) own init method
        super().__init__()   # Trying to call the init of super classes (A,B) 
        print("in C init")
    def feature5(self):
        print("feature5 is updated")    
    def feature6(self):
        print("feature6 is updated")

# creating the objects 
c1 = C()
# calling the normal methods
c1.feature1() 
 



    

    