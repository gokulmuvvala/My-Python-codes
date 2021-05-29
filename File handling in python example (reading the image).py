# File handling in python example (Image reading)
# open is a inbuilt function
# creating f,f1 variables
f = open('snow.jpg','rb')  # open(filename.type,mode) (rb means readbinary mode) 
f1 = open('mydog.jpg','wb') # creating a new image file of snow.jpg (wb means writebinary mode) 
for i in f:
    f1.write(i)
