# -------------------------------
# Step 1: Object-Oriented Programming (OOP)
# -------------------------------

class Student:
    # Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method to display details
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

    # Method to check result
    def result(self):
        return "Pass" if self.marks >= 40 else "Fail"


# Creating objects
s1 = Student("Rasna", 85)
s2 = Student("Amit", 35)

# Calling methods
print("---- Student Details ----")
s1.display()
print("Result:", s1.result())

print()
s2.display()
print("Result:", s2.result())


# -------------------------------
# Step 2: Exception Handling
# -------------------------------

print("\n---- Exception Handling ----")
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except ValueError:
    print("Error: Please enter valid integers")

finally:
    print("Execution completed")


# -------------------------------
# Step 3: File Operations
# -------------------------------

print("\n---- File Operations ----")

# A) Write Data to File
try:
    with open("students.txt", "w") as file:
        file.write("Name: Rasna\n")
        file.write("Marks: 85\n")
    print("Data written successfully")

except IOError:
    print("File write error")


# B) Read Data from File
try:
    with open("students.txt", "r") as file:
        content = file.read()
        print("\nFile Content:\n", content)

except FileNotFoundError:
    print("File not found")


# C) Append Data to File
try:
    with open("students.txt", "a") as file:
        file.write("Result: Pass\n")
    print("Data appended successfully")

except IOError:
    print("File write error")