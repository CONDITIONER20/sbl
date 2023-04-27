def calculate_grade(score):
    try:
        score = float(score)
    except ValueError:
        print("Invalid input! Please enter a numerical value.")
        return

    if score < 0 or score > 100:
        print("Invalid input! Score must be between 0 and 100.")
        return

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = input("Enter the score: ")
grade = calculate_grade(score)
if grade:
    print("The grade is:", grade)
