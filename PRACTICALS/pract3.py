#PRACT-3...

# SUB. LIST...
subjects = ["MATHS", "SCIENCE", "ENGLISH", "HISTORY", "COMPUTER"]

raw_students = []

for i in range(1, 11):
    print(f"\nSTUDENT {i} DETAILS:")
    roll = int(input("  ENTER ROLL NO.: "))
    name = input("  ENTER NAME: ")

    temp_marks = []
    print("  ENTER MARKS FOR 5 SUBJECTS (OUT OF 100):")
    for sub in subjects:
        m = int(input(f"    - {sub}: "))
        temp_marks.append(m)

    marks_tuple = tuple(temp_marks)

    raw_students.append({"ROLL": roll, "NAME": name, "MARKS": marks_tuple})


processed_students = []

for student in raw_students:
    total = sum(student["MARKS"])
    percentage = total / 5.0

    if percentage >= 85:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 55:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    student_record = {
        "ROLL": student["ROLL"],
        "NAME": student["NAME"],
        "MARKS": student["MARKS"],
        "TOTAL": total,
        "PERCENTAGE": percentage,
        "GRADE": grade,
    }
    processed_students.append(student_record)

seen_names = set()
duplicate_names = []
unique_students = []

for student in processed_students:
    if student["NAME"] in seen_names:
        duplicate_names.append(student["NAME"])
    else:
        seen_names.add(student["NAME"])
        unique_students.append(student)


class_avg_percentage = sum(s["PERCENTAGE"] for s in unique_students) / len(
    unique_students
)


max_percent = max(s["PERCENTAGE"] for s in unique_students)
min_percent = min(s["PERCENTAGE"] for s in unique_students)

highest_scorers = [
    s["NAME"] for s in unique_students if s["PERCENTAGE"] == max_percent
]
lowest_scorers = [
    s["NAME"] for s in unique_students if s["PERCENTAGE"] == min_percent
]

above_avg_students = [
    s["NAME"] for s in unique_students if s["PERCENTAGE"] > class_avg_percentage
]

failed_students = []
for s in unique_students:
    has_failed = False
    for m in s["MARKS"]:
        if m < 40:
            has_failed = True
            break
    if has_failed:
        failed_students.append(s["NAME"])

grade_dict = {"A": [], "B": [], "C": [], "D": [], "F": []}
for s in unique_students:
    grade_dict[s["GRADE"]].append(s["NAME"])


alphabetical_names = sorted([s["NAME"] for s in unique_students])


highest = -1
second_highest = -1

for s in unique_students:
    p = s["PERCENTAGE"]
    if p > highest:
        second_highest = highest
        highest = p
    elif p > second_highest and p != highest:
        second_highest = p

second_highest_scorers = [
    s["NAME"] for s in unique_students if s["PERCENTAGE"] == second_highest
]


subject_totals = [0, 0, 0, 0, 0]

for s in unique_students:
    for idx in range(5):
        subject_totals[idx] += s["MARKS"][idx]

subject_averages = [tot / len(unique_students) for tot in subject_totals]
max_sub_avg = max(subject_averages)
best_subject_name = subjects[subject_averages.index(max_sub_avg)]

# DISPLAY...
print("\n" + "=" * 65)
print("            STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 65)

print(f"{'ROLL':<6}{'NAME':<12}{'TOTAL':<8}{'PERCENTAGE':<14}{'GRADE':<6}")
print("-" * 65)
for s in unique_students:
    print(
        f"{s['ROLL']:<6}{s['NAME']:<12}{s['TOTAL']:<8}{s['PERCENTAGE']:<14.2f}{s['GRADE']:<6}"
    )

print("=" * 65)
print("                    ANALYTICS REPORT")
print("=" * 65)

print(f"1. CLASS AVERAGE PERCENTAGE   : {class_avg_percentage:.2f}%")
print(
    f"2. HIGHEST SCORER(S)          : {', '.join(highest_scorers)} ({max_percent:.2f}%)"
)
print(
    f"3. LOWEST SCORER(S)           : {', '.join(lowest_scorers)} ({min_percent:.2f}%)"
)
print(
    f"4. ABOVE CLASS AVG STUDENTS   : {', '.join(above_avg_students) if above_avg_students else 'NONE'}"
)
print(
    f"5. FAILED IN >=1 SUBJECT(S)   : {', '.join(failed_students) if failed_students else 'NONE'}"
)
print("-" * 65)
print("6. GRADE WISE MAPPING DICT    :")
for grade_key, names_list in grade_dict.items():
    print(f"   - GRADE '{grade_key}': {names_list}")

print("-" * 65)
print(f"7. ALPHABETICAL NAMES LIST    : {alphabetical_names}")
print(
    f"8. SECOND HIGHEST SCORER(S)   : {', '.join(second_highest_scorers) if second_highest > 0 else 'N/A'} ({second_highest:.2f}%)"
)
print(
    f"9. BEST AVERAGE SUBJECT       : {best_subject_name} (AVG: {max_sub_avg:.2f} MARKS)"
)
print(
    f"10. DUPLICATES FOUND & REMOVED: {duplicate_names if duplicate_names else 'NONE'}"
)
print("=" * 65)
