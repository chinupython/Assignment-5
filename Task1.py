marks = {'mike': 90, 'alice': 85, 'jake': 91}

try:
    name = input("Enter the student's name: ")
    print(name, "'s marks:", marks[name])
except KeyError:
    print("Student not found .")
