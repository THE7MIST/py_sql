# ------------------ LIST INITIALIZATION ------------------

marks = [89, 89, 25, 65, 48, 79, 35, 54]

# Print full list
print("Original list:", marks)
# Output: [89, 89, 25, 65, 48, 79, 35, 54]


# ------------------ ACCESSING ELEMENTS ------------------

print("Last element:", marks[-1])
# Output: 54

print("First element:", marks[0])
# Output: 89

print("Element at index 2:", marks[2])
# Output: 25

print("First 5 elements:", marks[0:5])
# Output: [89, 89, 25, 65, 48]


# ------------------ ITERATION USING FOR LOOP ------------------

print("All elements (for loop):")
for score in marks:
    print(score, end=" ")
# Output: 89 89 25 65 48 79 35 54

print()  # newline


# ------------------ LIST MODIFICATION ------------------

# Append element at end
marks.append(100)
print("After append:", marks)
# Output: [89, 89, 25, 65, 48, 79, 35, 54, 100]

# Insert element at specific index
marks.insert(2, 654)
print("After insert at index 2:", marks)
# Output: [89, 89, 654, 25, 65, 48, 79, 35, 54, 100]


# ------------------ MEMBERSHIP CHECK ------------------

print("Is 100 in list:", 100 in marks)
# Output: True

print("Is 47 in list:", 47 in marks)
# Output: False


# ------------------ LENGTH OF LIST ------------------

print("Length:", len(marks))
# Output: 10


# ------------------ ITERATION USING WHILE LOOP ------------------

i = 0
print("All elements (while loop):")
while i < len(marks):
    print(marks[i], end="    ")
    i += 1

# Output:
# 89    89    654    25    65    48    79    35    54    100

print()  # newline


# ------------------ ADDITIONAL LIST OPERATIONS ------------------

# Remove element (first occurrence)
marks.remove(89)
print("After removing 89:", marks)
# Output: [89, 654, 25, 65, 48, 79, 35, 54, 100]

# Pop last element
marks.pop()
print("After pop:", marks)
# Output: [89, 654, 25, 65, 48, 79, 35, 54]

# Sort list
marks.sort()
print("Sorted list:", marks)
# Output: [25, 35, 48, 54, 65, 79, 89, 654]

# Reverse list
marks.reverse()
print("Reversed list:", marks)
# Output: [654, 89, 79, 65, 54, 48, 35, 25]

# Count occurrences
print("Count of 89:", marks.count(89))
# Output: 1


# ------------------ CLEAR LIST ------------------

marks.clear()
print("After clear:", marks)
# Output: []