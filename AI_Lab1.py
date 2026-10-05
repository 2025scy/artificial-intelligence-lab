# Lab 1 - All Programs in One File


def program_1():
    # Percentage Calculator
    total_marks = float(input("Enter Total Marks: "))
    obtained_marks = float(input("Enter Obtained Marks: "))
    percentage = (obtained_marks / total_marks) * 100

    print("Total Marks:", total_marks)
    print("Obtained Marks:", obtained_marks)
    print("Percentage:", percentage, "%")


def program_2():
    # Percentage and Grade Calculator
    total_marks = float(input("Enter Total Marks: "))
    obtained_marks = float(input("Enter Obtained Marks: "))

    percentage = (obtained_marks / total_marks) * 100

    print("Percentage:", percentage, "%")

    if percentage >= 90:
        grade = "A"
        print("Grade:", grade)
        print("Outstanding")
    elif percentage >= 80:
        grade = "B"
        print("Grade:", grade)
    elif percentage >= 70:
        grade = "C"
        print("Grade:", grade)
    elif percentage >= 60:
        grade = "D"
        print("Grade:", grade)
    else:
        grade = "F"
        print("Grade:", grade)


def program_3():
    # Lab Attendance -> Marks
    c = int(input("Enter Lab Attendance: "))
    if c == 1:
        print("Marks = 10")
    elif c == 2:
        print("Marks = 20")
    elif c == 3:
        print("Marks = 30")
    elif c == 4:
        print("Marks = 40")
    elif c == 5:
        print("Marks = 50")


def program_4():
    # Lists: class_list and marks
    class_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

    result = marks[0] / class_list[0]

    print("Result =", result)

    final = 5 * result
    print("Final =", final)


def main():
    while True:
        print("\n===== Lab 1 Programs =====")
        print("1. Percentage Calculator")
        print("2. Percentage and Grade Calculator")
        print("3. Lab Attendance Marks")
        print("4. Class List and Marks")
        print("0. Exit")

        choice = input("Choose a program (0-4): ")

        if choice == "1":
            program_1()
        elif choice == "2":
            program_2()
        elif choice == "3":
            program_3()
        elif choice == "4":
            program_4()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
