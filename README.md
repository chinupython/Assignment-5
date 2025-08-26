Python Programs – Student Marks & List Operations


#Student Marks Finder
Problem Statement

Create a dictionary with student names as keys and their marks as values.

Ask the user to enter a student's name.

Display the marks if the student exists, otherwise show a message.

#Code
marks = {'mike': 90, 'alice': 85, 'jake': 91}

try:
    name = input("Enter the student's name: ")
    print(name, "'s marks:", marks[name])
except KeyError:
    print("Student not found in the record.")

Sample Run
Enter the student's name: mike
mike 's marks: 90

Enter the student's name: sam
Student not found in the record.



#Extract & Reverse List Elements
Problem Statement

Create a list of numbers from 1 to 10.

Extract the first five elements.

Reverse the extracted list.

#Code (using .reverse())
numbers = [1,2,3,4,5,6,7,8,9,10]

print("Original list:", numbers)

# Extract first 5 elements
list1 = numbers[0:5]
print("Extracted first five elements:", list1)

# Reverse in-place using .reverse()
list1.reverse()
print("Reversed extracted elements:", list1)

Sample Run
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
