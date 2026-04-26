# ------------------ SET INITIALIZATION ------------------

t = {"1", 3, 5, "sham"}

print("Type of t:", type(t))
# Output: <class 'set'>


marks = {95, 98, 65, 24, 2, 4, 65, 35, 35, 35, 87, 35, 62, 78, 70, 54}

print("Type of marks:", type(marks))
# Output: <class 'set'>


# ------------------ UNIQUE ELEMENTS ------------------

print("Marks set (duplicates removed):", marks)
# Output (order may vary):
# {65, 35, 2, 4, 70, 98, 78, 48?, ...}  ← only unique values


# ------------------ LIST TO SET ------------------

marks_2 = [89, 89, 25, 25, 25, 25, 65, 48, 79, 35, 54]

marks_3 = set(marks_2)

print("Converted list to set:", marks_3)
# Output (order may vary):
# {65, 35, 79, 48, 54, 89, 25}


# ------------------ PRINT ORIGINAL SET AGAIN ------------------

print("Marks set again:", marks)
# Output: same unique elements (order may differ)


# ------------------ ITERATION ------------------

print("Iterating through marks:")
for score in marks:
    print(score, end=" ")

# Output:
# Elements printed in random order


print()  # newline


# ------------------ ADDITIONAL SET OPERATIONS ------------------

# Add element
marks.add(100)
print("After adding 100:", marks)
# Output: includes 100

# Remove element
marks.remove(2)
print("After removing 2:", marks)
# Output: 2 removed

# Discard (safe remove)
marks.discard(999)  # no error if not found
print("After discard 999:", marks)
# Output: unchanged

# Membership check
print("Is 35 in marks:", 35 in marks)
# Output: True

print("Is 200 in marks:", 200 in marks)
# Output: False

# Length
print("Length of set:", len(marks))
# Output: number of unique elements


# ------------------ SET OPERATIONS ------------------

other = {35, 70, 200}

print("Union:", marks.union(other))
# Output: all unique elements combined

print("Intersection:", marks.intersection(other))
# Output: {35, 70}

print("Difference:", marks.difference(other))
# Output: elements in marks but not in other


# ------------------ CONVERT SET TO LIST ------------------

marks_list = list(marks)
print("Converted to list:", marks_list)
# Output: order may vary