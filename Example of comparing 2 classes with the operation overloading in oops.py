# example of comparing 2 classes with the of operation overloading
# defining classe
class student:
    # declaring the variables
    def __init__(self,m1,m2): # m1 and m2 are 2 subjects
        self.m1 = m1 
        self.m2 = m2
# Operation Overload for compaerison of s1 and s2
    def __gt__(self,other): # self for 1 class and other of 2nd class (gt represnts greater than )
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
           return True
        else:
           return False 
# creating the objects

s1 = student(83,56)
s2 = student(43,97)

if  s1 > s2: 
    print ("s1 is graeter than s2 ")
elif s1 < s2:
     print (" s2 is greater than s1 ")
else:
    print("Both s1 and s2 are equal")
