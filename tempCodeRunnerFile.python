# linear search with for loop 
pos = -1 # Here pos is a global variable and we are intiating with the -1 it is used to find the position of the n in the list 
# user defined function defininition
def search(lst,n):
  i = 0 # intially assigning i=0 

# using for loop for logic
  for  i in range(len(lst)):
      if lst[i] == n:
        globals()['pos'] = i # Using global keyword because the pos global variable 
        return True

  return False  


lst = [1, 99, 5, 9, 6, 14]
n = int(input("Enter the number to search = ")) #n is The number  we need search

if search(lst,n):  # user defined function syntax is search(list,n) # variable name can be changed 
   print ("Found")

else:
    print("Not found")




