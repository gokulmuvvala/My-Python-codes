# factorial of number using recursion 
n = int(input("Enter the number = "))
def fact(n):
    if n == 0: # we know that factorial of 0 is 1 
        return 1

 
    
    return n * fact(n-1) # number x fact(number-1)       
result=fact(n)

print(result)

    