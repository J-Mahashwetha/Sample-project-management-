# main.py
# Grade Calculator Program

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def main():
    print("🎓 Student Grade Calculator 🎓")
    name = input("Enter student name: ")
    marks = float(input("Enter total marks (out of 100): "))
    grade = calculate_grade(marks)
    print(f"{name}'s Grade: {grade}")

if __name__ == "__main__":
    main()
