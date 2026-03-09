student = {"Alice": 85, "Mark": 80, "Steve": 79, "Mary": 68} # create a dictionary with student details.
student_name = input("Enter the student name: ").capitalize() # prompt user to enter a student name
if student_name in student: # check wheather student name present in the dictionary.
    print(f"{student_name}'s mark: {student[student_name]}")
else:
    print(f"Student not found.")
