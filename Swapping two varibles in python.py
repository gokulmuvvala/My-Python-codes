# swapping two variables in python in different method
a = 5
b = 20

# type 1 
temp = a
a = b
b = temp
print (a)
print (b)

# type 2 
a = a + b
b = a - b
a = a - b
print (a)
print (b)

# type 3
a = a ^ b
b = a ^ b
a = a ^ b
print (a)
print (b)

# type 4
a,b =b,a 
print (a)
print (b)
