class StudentManager:
    def __init__(self, filename):
        self.filename = filename

    def add_student(self, name, marks):
        try:
            marks = int(marks)
            if marks < 0 or marks > 100:
                raise ValueError("Marks must be between 0 and 100") # raise is used to throw exception that is not caught by python.

            with open(self.filename, "a") as f:
                f.write(f"{name},{marks}\n") #insert variables directly inside a string. f-string.

            print("Student record added successfully")

        except ValueError as ve:
            print("Input Error:", ve)

        except IOError:
            print("File error occurred while writing")

    def display_students(self):
        try:
            with open(self.filename, "r") as f:
                print("\nStudent Records:")
                for line in f:
                    name, marks = line.strip().split(",") #strip removes whitespace and split string in list values separating by ,
                    print(f"Name: {name}, Marks: {marks}") #formatted string (f-string)

        except FileNotFoundError:
            print("No records found. File does not exist.")

        except Exception as e:
            print("Unexpected error:", e)


# -------- Main Program --------
manager = StudentManager("students1.txt")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        manager.add_student(name, marks)

    elif choice == "2":
        manager.display_students()

    elif choice == "3":
        print("Program exited")
        break

    else:
        print("Invalid choice")
