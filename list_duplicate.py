# 5:
# - Write a Python program that removes all duplicates from a given list and prints the new list without duplicates.

int_list = [99,78,99,12,19,24,19]
print(int_list)
for x in int_list:
    if int_list.count(x)>1:
        int_list.remove(x)
print(int_list)



