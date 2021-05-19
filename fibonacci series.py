# fibonacci sequence
n  = int(input("How many terms? "))
def fib(n):
    a = 0
    b = 1
    if n == 1:
       print(a)
    elif n == 0:
         print("error [Enter any other number]")   
    elif n<0:
        print ("error [Enter any postive number]")

    else:
          print (a)
          print (b)

    for i in range(2,n):
        c = a + b
        a = b
        b = c 
        print(c)

fib(n)

