# ------------------ OPEN FILE (READ MODE) ------------------

f = open("demo.txt", "rt")   # 'r' = read, 't' = text mode (default)

# Read entire file content
data = f.read()

print("File content:")
print(data)
# Output: (contents of demo.txt)


# ------------------ WRITE OPERATION NOTE ------------------

# f.write("this will overwrite all data")
# ❌ Error here because file is opened in read mode ('r')
# To write, file must be opened in 'w' or 'a' mode


# ------------------ OPEN FILE (APPEND MODE) ------------------

s = open("sample.txt", "a")   # 'a' = append mode (creates file if not exist)

# Append new data
s.write("New line added\n")

print("Data appended to sample.txt")
# Output: Data appended to sample.txt


# ------------------ CLOSE FILES ------------------

f.close()
s.close()


# ------------------ ADDITIONAL FILE OPERATIONS ------------------

# 1. Read line by line
f = open("demo.txt", "r")
print("Reading line by line:")
for line in f:
    print(line.strip())
f.close()


# 2. Write mode (overwrites file)
w = open("sample.txt", "w")
w.write("This will overwrite existing content\n")
w.close()
# Output: sample.txt content replaced


# 3. Using 'with' (best practice - auto close)

with open("demo.txt", "r") as file:
    content = file.read()
    print("Using with:", content)
# File automatically closed


# 4. Check file modes summary
# 'r' → read (error if file not found)
# 'w' → write (overwrite/create)
# 'a' → append (add/create)
# 'x' → create (error if exists)