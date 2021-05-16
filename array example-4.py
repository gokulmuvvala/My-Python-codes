from array import *
arr = array('i',[]) # A empty array is created 
n = int(input("Enter the length of an array =")) # taking length of array from user
# entering the elements from user
for i in range(n):
    x = int(input("Enter the next value = "))
    arr.append(x)  # adding the elements into the array 
print(arr)
 
# 1st method
   # comparing the elements in the array
val =  int(input("Enter the value to search ="))
k=0 # declaring k variable as empty variable
for e in arr:
    if e==val:
        print(k) # here if searched element is found in array then we will print the index value of array 
        break
    k+=1
    # 2nd method for finding the element in array by using in-build function  
print (arr.index(val))





