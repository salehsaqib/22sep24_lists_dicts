# 3:
# - Write a program that takes a list of student names as input, sorts the names in alphabetical order, and prints the sorted list.

# -------------------------- First Way ------------------------------------------
# stu_list:str = str(input("Enter list of Students: e.g ['Shahid','Imran','Ali'] : "))
# my_list = eval(stu_list)
# print(my_list)
# my_list.sort()
# print(my_list)


# -------------------------- Second Way ------------------------------------------
stu:list = []
while True:
    list_item:str = str(input("Add Student Name to List: (Enter 'S' to show in Sorting)  "))
    if list_item=='S' or list_item=='s':
        break
    else:
        stu.append(list_item)
print(stu)
stu.sort()
print(stu)