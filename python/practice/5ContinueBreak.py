# ------------------ LIST INITIALIZATION ------------------

students = ['ram', 'sham', 'gita', 'sita', 'ghansham', 'asd', 'aefh']

# Check datatype
print("Type:", type(students))
# Output: <class 'list'>


# ------------------ EXAMPLE 1: break ------------------

# Stops loop completely when condition is met
print("Using break:")
for s in students:
    if s == 'ghansham':
        break
    print(s, end=" ")

print()
# Output: ram sham gita sita


# ------------------ EXAMPLE 2: continue ------------------

# Skips only the matched iteration
print("Using continue:")
for s in students:
    if s == 'ghansham':
        continue
    print(s, end=" ")

print()
# Output: ram sham gita sita asd aefh


# ------------------ ADDITIONAL EXAMPLES ------------------

# 1. Using else with for loop
print("For-else example:")
for s in students:
    if s == 'xyz':
        print("Found")
        break
else:
    print("Not found")

# Output: Not found


# 2. Using enumerate (index + value)
print("Enumerate:")
for index, name in enumerate(students):
    print(index, name)

# Output:
# 0 ram
# 1 sham
# 2 gita
# 3 sita
# 4 ghansham
# 5 asd
# 6 aefh


# 3. Filtering using condition
print("Names starting with 'a':")
for s in students:
    if s.startswith('a'):
        print(s, end=" ")

print()
# Output: asd aefh


# 4. Counting specific element
count = 0
for s in students:
    if s == 'sham':
        count += 1

print("Count of 'sham':", count)
# Output: 1


# 5. Reverse iteration
print("Reverse order:")
for s in reversed(students):
    print(s, end=" ")

print()
# Output: aefh asd ghansham sita gita sham ram