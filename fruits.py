# 2:
# Given a list of fruits: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango'], write a program to:
# Access the first, middle, and last element of the list.
# Change the second element to 'blueberry'.

fruits:list = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
print(fruits)
print("The First Element in the list is : ",fruits[0])
fruits_len:int = len(fruits)-1
middle_val:int = int(len(fruits)/2)
print("The Middle Element in the list is : ",fruits[middle_val])
print("The Last Element in the list is : ",fruits[fruits_len])
fruits[1]='blueberry'
print(fruits)