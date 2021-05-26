# iterator example
# defining the list
nums = [1, 2, 3, 4, 5] 

it = iter(nums)

# printing the iterator 
print(it.__next__())
print(it.__next__())
# we can also write like this 
print(next(it))
# we can also by using the for loop also
for i in nums:
    print(i)
