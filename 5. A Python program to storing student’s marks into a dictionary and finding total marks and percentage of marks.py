marks = {"Shwetal": [70, 80, 90], "Naufil": [60, 70, 80], "Tanmay": [80, 90, 100]}
for student, mark_list in marks.items():
    total_marks = sum(mark_list)
    percentage = total_marks / len(mark_list)
    print(student + ":")
    print("Total marks:", total_marks)
    print("Percentage:", percentage)
