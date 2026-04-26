# ------------------ TUPLE INITIALIZATION ------------------

t = ("1", 3, 5, "sham")

print("Type of t:", type(t))
# Output: <class 'tuple'>


marks = (95, 98, 65, 24, 2, 4, 65, 35, 35, 35, 87, 35, 62, 78, 70, 54)

print("Type of marks:", type(marks))
# Output: <class 'tuple'>


# ------------------ IMMUTABILITY ------------------

# marks[0] = 99
# ❌ Error: 'tuple' object does not support item assignment
# Tuples are immutable (cannot be changed after creation)


# ------------------ BUILT-IN METHODS ------------------

# Count occurrences of 35
print("Count of 35:", marks.count(35))
# Output: 4

print("Type of count result:", type(marks.count(35)))
# Output: <class 'int'>

# Find index of first occurrence of 95
print("Index of 95:", marks.index(95))
# Output: 0


# ------------------ ADDITIONAL TUPLE OPERATIONS ------------------

# Accessing elements
print("First element:", marks[0])
# Output: 95

print("Last element:", marks[-1])
# Output: 54

# Slicing
print("First 5 elements:", marks[0:5])
# Output: (95, 98, 65, 24, 2)

# Membership check
print("Is 65 in tuple:", 65 in marks)
# Output: True

print("Is 100 in tuple:", 100 in marks)
# Output: False

# Length
print("Length of tuple:", len(marks))
# Output: 16

# Iteration
print("Elements in tuple:")
for item in marks:
    print(item, end=" ")
# Output: 95 98 65 24 2 4 65 35 35 35 87 35 62 78 70 54

print()  # newline


# ------------------ CONVERSION OPERATIONS ------------------

# Convert tuple to list (to modify)
marks_list = list(marks)
marks_list.append(999)

print("After converting to list and appending:", marks_list)
# Output: [95, 98, 65, 24, 2, 4, 65, 35, 35, 35, 87, 35, 62, 78, 70, 54, 999]

# Convert back to tuple
marks = tuple(marks_list)
print("Converted back to tuple:", marks)
# Output: (95, 98, 65, 24, 2, 4, 65, 35, 35, 35, 87, 35, 62, 78, 70, 54, 999)


# ------------------ UNPACKING ------------------

a, b, c, *rest = marks
print("Unpacked values:", a, b, c)
# Output: 95 98 65

print("Remaining elements:", rest)
# Output: [24, 2, 4, 65, 35, 35, 35, 87, 35, 62, 78, 70, 54, 999]