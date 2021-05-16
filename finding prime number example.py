# finding prime number
num = 1

flag = False
if num >1:
    for i in range (2, num):
        if (num % i) == 0:
           flag= True
        break



if flag:
        print(num,"Not a Prime number")

else:
        print(num,"Yes Prime number")
