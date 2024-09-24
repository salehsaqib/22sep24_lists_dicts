# 8:
# - Write a program that creates a dictionary where the keys are subjects (e.g., 'Math', 'Science') 
# and the values are lists of marks. Add marks for 3 subjects, and print the average marks for each subject.

average_marks = {
    "English": 90,
    "Urdu": 75,
    "Math": 100    
}
sum:int = 0
count:int = 0
for x in average_marks:
    sum += int(average_marks[x])
    count +=1
print(f"The Average Marks of {count} Subjects =  {int(sum/count)}")