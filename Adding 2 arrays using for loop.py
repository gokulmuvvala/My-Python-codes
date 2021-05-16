from numpy import *
arr1 = array([5,79,12,6,7,9,4,2])
arr2 = array([8,96,36,9,5,7,6,8])
arr3 = ([]) # empty array is created
k=0 # k is a temp variable
for num1 in arr1:
                num3 = num1 + arr2[k]
                arr3.append(num3)
                k +=1
                print(arr3)
