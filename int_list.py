# 4:
# - Write a program that takes a list of integers and prints:
# The first 3 elements
# The last 2 elements
# The entire list in reverse order

int_list = [45,78,3,12,99,56,29]
print(int_list)
print("The First Three Elements")
for x in range(3):
    print(int_list[x],end=" ")
print("\nThe Last Two Elements")
i:int = len(int_list)-1
loop_counter:int = 1
while loop_counter <= 2:
    print(int_list[i],end=" ")
    loop_counter +=1
    i -=1
print("\nThe list in Reverse Order")
int_list.sort(reverse=True)
print(int_list)



