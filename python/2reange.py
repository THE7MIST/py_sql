# Range Initialization
number = range(4, 9)

# Printing the range object
print("Range object:", number)
# Output: range(4, 9)

# Converting range to list (to see actual values)
print("List:", list(number))
# Output: [4, 5, 6, 7, 8]

# Iterating through range
print("Elements in range:")
for i in number:
    print(i, end=" ")
# Output: 4 5 6 7 8

print()  # for newline


# ------------------ Additional Range Operations ------------------

# Using step in range
step_range = range(4, 9, 2)
print("Range with step 2:", list(step_range))
# Output: [4, 6, 8]

# Reverse range
reverse_range = range(9, 3, -1)
print("Reverse range:", list(reverse_range))
# Output: [9, 8, 7, 6, 5, 4]

# Length of range
print("Length of range:", len(number))
# Output: 5

# Membership check
print("Is 6 in range:", 6 in number)
# Output: True

print("Is 10 in range:", 10 in number)
# Output: False

# Indexing (convert to list first)
num_list = list(number)
print("Element at index 2:", num_list[2])
# Output: 6

# Sum of elements
print("Sum of range:", sum(number))
# Output: 30

# Min and Max
print("Minimum:", min(number))
# Output: 4

print("Maximum:", max(number))
# Output: 8