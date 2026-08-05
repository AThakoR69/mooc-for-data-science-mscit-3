
''' PRACT-1 :VARIABLES --- > ROLLNO., NAME, AGE, MARKS
 CALCULATE TOTAL,PERCENTAGE
 40 MARKS <= PASS
 FORMATE OUTPUT 
 USE COMMENTS... '''


# USER INPUT...
total_students = int(input("HOW MANY STUDENTS DATA DO YOU WANT ? : "))

# LOOP FOR MULTIPLE STUDENTS...
for i in range(1, total_students + 1):
    print(f"\n---> ENTER DETAILS FOR STUDENTS {i} <---")
    
    # GET STUDENTS INFO...
    roll_no = int(input("ENTER ROLL NO.: "))
    name = input("ENTER NAME: ")
    age = int(input("ENTER AGE: "))
    
    # MARKS OF SUB. ...
    maths = int(input("ENTER MATHS MARKS: "))
    science = int(input("ENTER SCIENCE MARKS: "))
    english = int(input("ENTER ENGLISH MARKS: "))
    
    # TOTAL  MARKS AND PRECENTAGE...
    total_marks = maths + science + english
    percentage = total_marks / 3
    
    # PASS-FAIL...
    is_passed = (maths >= 40) and (science >= 40) and (english >= 40)
    
    # DIPSLAY
    print("\n========================================")
    print(f"        REPORT CARD FOR STUDENT {i}")
    print(f"========================================")
    print(f"ROLL NO.    : {roll_no}")
    print(f"NAME        : {name}")
    print(f"AGE         : {age}")
    print("----------------------------------------")
    print(f"MATHS       : {maths}")
    print(f"SCIENCE     : {science}")
    print(f"ENGLISH     : {english}")
    print("----------------------------------------")
    print(f"TOTAL MARKS : {total_marks} / 300")
    print(f"PERCENTAGE  : {percentage:.2f}%")
    
    # CHECK RESULT...
    if is_passed:
        print("RESULT      : PASSED")
    else:
        print("RESULT      : FAILED")
    print("========================================")
