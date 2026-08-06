''' PRACT-2 :
Create a Python program to
● Store marks of 10 students in a list.
● Convert the list into tuples.
● Store student names and marks in a dictionary.
● Find:
○ Highest marks
○ Lowest marks
○ Average marks
● Display students scoring above average.
● Remove duplicate marks using sets '''


marks_list = [85, 92, 78, 85, 90, 65, 78, 88, 92, 70]

marks_tuple = tuple(marks_list)


student_dict = {
    "SKY": 85,
    "OMPURI": 92,
    "ANIL": 69,
    "NARESH": 71,
    "KINJAL": 90,
    "PRATHNA": 65,
    "FARHAN": 78,
    "HONEY": 88,
    "DHARMESH": 92,
    "URVSHI": 69
}

highest_marks = max(marks_list)
lowest_marks = min(marks_list)
average_marks = sum(marks_list) / len(marks_list)

print("=======> STUDENT MARKS ANALYSIS <=======")
print(f"MARKS LIST    : {marks_list}")
print(f"MARKS TUPLE   : {marks_tuple}")
print(f"HIGHEST MARKS : {highest_marks}")
print(f"LOWEST MARKS  : {lowest_marks}")
print(f"AVERAGE MARKS : {average_marks:.2f}")

print("STUDENTS SCORING ABOVE AVERAGE :")
for name, mark in student_dict.items():
    if mark > average_marks:
        print(f"  - {name}: {mark}")


unique_marks = set(marks_list)
print(f"UNIQUE MARKS (DUPLICATES REMOVED) : {unique_marks}")
