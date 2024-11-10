"""Write a Python program to create a list of 5 numbers. Add an element to the list, remove one element, and find the maximum and minimum number in the list.

Given a list of fruits: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango'], write a program to:

Access the first, middle, and last element of the list.
Change the second element to 'blueberry'.

- Write a program that takes a list of student names as input, sorts the names in alphabetical order, and prints the sorted list.
- Write a program that takes a list of integers and prints:

The first 3 elements
The last 2 elements
The entire list in reverse order

- Write a Python program that removes all duplicates from a given list and prints the new list without duplicates.



- Create a dictionary where the keys are the names of 5 different countries and the values are their capitals. Write a program to display all the countries and their capitals.
- Write a program to update the 'grade' value to 'A', and add a new key-value pair for 'major' with the value 'Computer Science'.
student = {'name': 'John', 'age': 22, 'grade': 'B'}

- rite a program that creates a dictionary where the keys are subjects (e.g., 'Math', 'Science') and the values are lists of marks. Add marks for 3 subjects, and print the average marks for each subject."""
## PYTHO LIST
dic = {1:"shahid",2:[10,20,30],'dic2':{'a':"shahid",'b':"javed"}}
print("Print before deletion of above item:")
print(dic)
print(type(dic))
print(dic[2][0])
print(dic['dic2']['a'])
del(dic[2][0])

print("PRINT AFTER DELETION :",dic)

print('''1 - Write a Python program to create a list of 5 numbers. Add an element to the list, remove one element, and find the maximum and minimum number in the list.''')
# Step 1: Create a list of 5 numbers
numbers = [10, 25, 8, 17, 30]
print("Original List:", numbers)

# Step 2: Add an element to the list
numbers.append(22)
print("List after adding an element:", numbers)

# Step 3: Remove one element from the list
numbers.remove(17)
print("List after removing an element:", numbers)

# Step 4: Find the maximum and minimum number in the list
max_number = max(numbers)
min_number = min(numbers)

print("Maximum number in the list:", max_number)
print("Minimum number in the list:", min_number)

print('''Given a list of fruits: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango'], write a program to:

Access the first, middle, and last element of the list.
Change the second element to 'blueberry'.
''')

# List of fruits
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']

# Access the first, middle, and last element
first_fruit = fruits[0]
middle_fruit = fruits[len(fruits) // 2]  # Integer division to get the middle index
last_fruit = fruits[-1]

print("First fruit:", first_fruit)
print("Middle fruit:", middle_fruit)
print("Last fruit:", last_fruit)

# Change the second element to 'blueberry'
fruits[1] = 'blueberry'
print("Updated list of fruits:", fruits)

print('''3 -  Write a program that takes a list of student names as input, sorts the names in alphabetical order, and prints the sorted list.
''')

# Input: List of student names
student_names = input("Enter the student names, separated by a comma: ").split(",")

# Remove leading and trailing whitespaces from each name
student_names = [name.strip() for name in student_names]

# Sort the list of names in alphabetical order
sorted_names = sorted(student_names)

# Print the sorted list of names
print("Sorted list of student names:", sorted_names)

print('''4 -  Write a program that takes a list of integers and prints:

The first 3 elements
The last 2 elements
The entire list in reverse order
''')

# Input: List of integers
integers = input("Enter a list of integers, separated by comma: ").split(',')

# Convert input from string to integers
integers = [int(num) for num in integers]

# Print the first 3 elements
print("First 3 elements:", integers[:3])

# Print the last 2 elements
print("Last 2 elements:", integers[-2:])

# Print the entire list in reverse order
print("List in reverse order:", integers[::-1])

print('''5 : Write a Python program that removes all duplicates from a given list and prints the new list without duplicates.
''')

# Remove duplicates while maintaining order
def remove_duplicates(original_list):
    new_list = []
    for item in original_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

# Given list with duplicates
original_list = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 5]

# Remove duplicates
new_list = remove_duplicates(original_list)

# Print the new list without duplicates
print("Original List:", original_list)
print("List without duplicates (maintaining order):", new_list)


print('''6 : Create a dictionary where the keys are the names of 5 different countries and the values are their capitals. Write a program to display all the countries and their capitals.''')
# Creating a dictionary with countries as keys and capitals as values
countries_and_capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Japan': 'Tokyo',
    'India': 'New Delhi',
    'Brazil': 'Brasilia'
}

# Displaying all countries and their capitals
print("Countries and their Capitals:")
for country, capital in countries_and_capitals.items():
    print(f"{country}: {capital}")

print ("""7 -  Write a program to update the 'grade' value to 'A', and add a new key-value pair for 'major' with the value 'Computer Science'.
student = {'name': 'John', 'age': 22, 'grade': 'B' """)

# Initial student dictionary
student = {'name': 'John', 'age': 22, 'grade': 'B'}

# Update the 'grade' to 'A'
student['grade'] = 'A'

# Add a new key-value pair for 'major'
student['major'] = 'Computer Science'

# Print the updated dictionary
print(student)
