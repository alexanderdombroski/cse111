# Team activity 2/5/24

from csv import reader

def read_file():
    with open("students.csv", "rt") as file:
        file = reader(file)
        next(file)

        student_directory = {}
        for line in file:
            student_directory[line[0]] = line[1]

        return student_directory

def main():
    student_directory = read_file()
    
    student = input("enter an i-number: ")
    for character in student:
        if character == "-":
            student = student.replace("-", "")

    if student in student_directory:
        print(student_directory[student])
    else:
        print("No such student")

main()