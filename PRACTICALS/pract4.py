# PRACT-4...

import numpy as np
import pandas as pd

# 1. BATCH & DATA LOADING FROM CSV...
batch_info = "Batch-2026-Computer_Science"
dept_name = batch_info.split("-")[2].replace("_", " ").upper()

subjects = ("MATHS", "SCIENCE", "ENGLISH", "HISTORY", "COMPUTER")

df = pd.read_csv("students.csv")

student_names = list(df["NAME"])
roll_numbers = list(df["ROLL"])

marks = df[list(subjects)].to_numpy()
.3/6

# 2. PERFORMANCE ANALYSIS (NUMPY OPERATIONS)...

totals = np.sum(marks, axis=1)
percentages = totals / 5.0

sub_averages = np.mean(marks, axis=0)

class_avg = np.mean(percentages)

best_idx = np.argmax(totals)
worst_idx = np.argmin(totals)

best_student = student_names[best_idx]
worst_student = student_names[worst_idx]

best_sub_idx = np.argmax(sub_averages)
worst_sub_idx = np.argmin(sub_averages)

best_subject = subjects[best_sub_idx]
worst_subject = subjects[worst_sub_idx]

sliced_marks = marks[:3, 3:5]

# 3. ANALYTICS & FILTERING

search_sub = "MATHS"
if search_sub in subjects:
    sub_index = subjects.index(search_sub)

distinction = []
for i in range(len(student_names)):
    if percentages[i] >= 85:
        distinction.append(student_names[i])

failed = []
for i in range(len(student_names)):
    if np.any(marks[i] < 40):
        failed.append(student_names[i])

above_avg = []
for i in range(len(student_names)):
    if percentages[i] > class_avg:
        above_avg.append(student_names[i])

reversed_names = list(reversed(student_names))
sorted_names = sorted(student_names)

# ==============================================================================
# 4. SUMMARY REPORT
# ==============================================================================
print("=" * 65)
print("               ACADEMIC PERFORMANCE SUMMARY REPORT")
print("=" * 65)
print(f"BATCH NAME                  : {batch_info}")
print(f"DEPARTMENT NAME             : {dept_name}")
print(f"TOTAL NUMBER OF STUDENTS    : {len(student_names)}")
print(f"OVERALL CLASS AVG PERCENTAGE: {class_avg:.2f}%")
print(
    f"HIGHEST SCORING STUDENT     : {best_student} ({percentages[best_idx]:.2f}%)"
)
print(
    f"LOWEST SCORING STUDENT      : {worst_student} ({percentages[worst_idx]:.2f}%)"
)
print(
    f"SUBJECT WITH HIGHEST AVG    : {best_subject} ({sub_averages[best_sub_idx]:.2f})"
)
print(
    f"SUBJECT WITH LOWEST AVG     : {worst_subject} ({sub_averages[worst_sub_idx]:.2f})"
)
print(f"NO. OF DISTINCTION HOLDERS  : {len(distinction)}")
print(f"NO. OF FAILED STUDENTS      : {len(failed)}")
print("=" * 65)

print("\n--- ADDITIONAL DETAILS ---")
print(f"DISTINCTION HOLDERS LIST    : {distinction}")
print(f"FAILED STUDENTS LIST        : {failed}")
print(f"ABOVE CLASS AVG STUDENTS    : {above_avg}")
print(f"REVERSED NAMES LIST         : {reversed_names}")
print(f"ALPHABETICAL NAMES LIST     : {sorted_names}")
print("\nSLICED MARKS (FIRST 3 STUDENTS, LAST 2 SUBJECTS):")
print(sliced_marks)
print("=" * 65)
