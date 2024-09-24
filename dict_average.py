# 8:
# - Write a program that creates a dictionary where the keys are subjects (e.g., 'Math', 'Science') 
# and the values are lists of marks. Add marks for 3 subjects, and print the average marks for each subject.

average_marks = {
    "English": [78,55,12,40,59,95,53,78],
    "Urdu": [78,23,45,96,75,45],
    "Math": [84,58,76,23,90,100]
}
for x in average_marks:
    print(f"Average Marks of {x} : ",end=" ")
    sum:int = 0
    count:int = 0
    for y in average_marks[x]:
        sum += y
        count +=1
    print(int(round((sum/count),0)))

