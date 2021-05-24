# single inheritance examaples in opps 
# defining the classes
class A: # super class (parent class)
# defining the methods
    def feature1(self):
        print("Feature 1 is working ")
    
    def feature2(self):
        print("Feature 2 is working ")
    
class B(A): # sub class (child class)
    def feature3(self):
        print("feature 3 is working")   
    def feature4(self):
        print("feature 4 is working")

# createing the object
a1 = A() # object 1

# calling the methods
a1.feature1()
a1.feature2()

# createing the object 
b1 = B() # object 2

# calling the methods
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()



