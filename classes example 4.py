# class example types of method
# In this example we will find the average all subjects 

# declareing the class

class student:
    # defining the static or class varibles
    school = "Sri chaitanaya high school"
    # defining the instance variables with the __init__ method
    def __init__(self,m1,adc,cmos,edc): # taking the input after the object is created 
        self.m1   = m1
        self.adc  = adc
        self.cmos = cmos
        self.edc  = edc

# defining the instance method for finding the average of the all subjects fof student
    def avg(self):
        return (self.m1+self.adc+self.cmos+self.edc)/3 
# defininig a class method 
    @classmethod # we need  decorators for using class method 
    def getschool(cls):  # cls represents class here
        return cls.school 
# definintg a static method 
    @staticmethod # we need  decorators for using  method 
    def info():
        return ("This is static method ... My name is gokul kumar")   
# creating a objects
s1 = student(22, 54, 63, 65) # s1 object is created 
s2 = student(56, 29, 64, 58) # s2 object is created
s3 = student(86, 91, 34, 22) # s3 object is created
# printing the averages here 
print(s1.avg())
print(s2.avg())
print(s3.avg())
# calling the class method here
print(student.getschool()) # here instead of student we can use s1,s2,s3
# calling the static method here
print(student.info()) # here instead of student we can use s1,s2,s3
