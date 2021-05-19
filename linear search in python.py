# linear search
pos = -1 # Here pos is a global variable and we are intiating with the -1 it is used to find the position of the n in the list 
# user defined function defininition
def search(list,n)
i = 0 # intially assigning i=0 
# using while loop for logic
while i<len(list)  # here we are using < only because the list starts from 0
if list[i] == n:
    globals()['pos'] = i # Using global keyword because the pos global variable 
    return True
    i = i +1 # incremention i for loop running purpose
return false  


lst = int(input("Enter thr list here = "))
n = 9 # The number 9 we need search


if search(lst,n):  # user defined function syntax is search(list,n) # variable name can be changed 
print ("Found")

else:
    print("Not found")




