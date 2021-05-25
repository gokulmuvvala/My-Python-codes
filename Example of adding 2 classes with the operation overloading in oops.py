# example of adding 2 classes with the of operation overloading
# defining classe

class student:
    # declaring the variables
    def __init__(self,m1,m2): # m1 and m2 are 2 subjects
        self.m1 = m1 
        self.m2 = m2
# Operation Overload for addition of 2 student Classes (defining a method of addition of 2 classes)
    def __add__(self,other): # self for 1 class and other of 2nd class
        m1 = self.m1 + other.m1
        m2 = self.m1 + other.m2
        s3 = student(m1,m2)
        return s3 
# creating the objects

s1 = student(33,56)
s2 = student(64,92)

s3 = s1 + s2

print(s3.m1) # here we are printing 33 + 64