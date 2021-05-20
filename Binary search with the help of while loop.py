# Binary search
pos = -1 # Here pos is a global variable and we are intiating with the -1 it is used to find the position of the n in the list 
# user defined function defininition
def search(lst, n):
  l = 0 # intially assigning lower bound = 0 
  u = len(lst)-1 # intially assigning upper bound = 0 
# using while loop for logic
  while l <= u: # lower bound is allways less than or equal to upper bound 
      mid = (l+u) // 2 # We need to find the mid value by the formula  ( Here we are using the integer division // )
      
      if lst[mid] == n: # if mid value is equal to searching value (n) 
          globals()['pos'] =  mid 
          return True 
      else:
         if lst[mid] < n: # if mid value is less than searching value (n). 
                 l = mid+1   # Make the mid value as lower value
         else: # if mid value is greater than searching value (n). 
                 u = mid-1    # Make the mid value as higher value
         return False

lst = [1, 99, 5, 9, 6, 14]
n = int(input("Enter the number to search = ")) #n is The number  we need search

if search(lst, n):  # user defined function syntax is search(list,n) # variable name can be changed 
   print ("Found at",pos+1)

else:
    print("Not found")




