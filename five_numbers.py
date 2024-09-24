# 1:
# Write a Python program to create a list of 5 numbers. 
# Add an element to the list, remove one element, and find the maximum and minimum number in the list.

nums:list = [45,10,112,99,5]
nums.append(56)
print(nums)
nums.pop()
print(nums)
gnum:int = nums[0]
for x in nums:
    if x > gnum:
        gnum = x
print(f"The Maximum Value is : {gnum}")
for x in nums:
    if x < gnum:
        gnum = x
print(f"The Minimum Value is : {gnum}")
