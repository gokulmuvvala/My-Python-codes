# File handling in python example (writing and appending the file content)
# open is a inbuilt function
# w means write mode 
# creating f variable
f = open('hello.txt','w')  # open(filename.type,mode) 
f = open('hello.txt','a')  # open(filename.type,mode) (a means append mode)
print(f.write("My pet name is snow ")) # write mode used to write inside the file
print(f.write( "My name is kumar")) # here we are adding the with the help of append


