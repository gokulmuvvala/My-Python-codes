# default Arguments
# declaring the function
def add(*b): # Formal arguments 
   c = 0 
   for i in b:
    c = c+i

# calling function
print(c)
add(2,15,3,4)   #Actual Arguments
