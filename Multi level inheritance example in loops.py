# multi level inheritance 
# defining classes
class A: # (parent class)
    def feature1(self):
        print("feature1 is updated")
    
    def feature2(self):
        print("feature2 is updated")

class B(A):  #(child class)
    def feature3(self):
        print("feature3 is updated")
    
    def feature4(self):
        print("feature4 is updated")
class C(B): # (child class of B)
    def feature5(self):
        print("feature5 is updated")
    
    def feature6(self):
        print("feature6 is updated")

# craeting the objects 
c1 = C()

# calling the mwthods
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()



    

    