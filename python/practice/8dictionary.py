# ------------------ DICTIONARY INITIALIZATION ------------------

marks = {
    "english": 95,
    "chem": 98,
    "phy": 89,
    "math": "not mathing"
}

# ------------------ ACCESSING VALUES ------------------

print("Chemistry marks:", marks["chem"])
# Output: 98

print("Math value:", marks["math"])
# Output: not mathing


# ------------------ KEY ERROR NOTE ------------------

# print(marks["maths"])
# ❌ KeyError: 'maths' (key does not exist)


# ------------------ ADD NEW KEY ------------------

marks["maths"] = 99

print("After adding 'maths':", marks)
# Output:
# {'english': 95, 'chem': 98, 'phy': 89, 'math': 'not mathing', 'maths': 99}


# ------------------ ADDITIONAL IMPROVEMENTS ------------------

# Safe access using get()
print("Get 'maths':", marks.get("maths"))
# Output: 99

print("Get 'bio' (not present):", marks.get("bio"))
# Output: None


# Check if key exists before accessing
if "maths" in marks:
    print("maths exists:", marks["maths"])
# Output: maths exists: 99


# Update existing key
marks["math"] = 90
print("After updating 'math':", marks)
# Output: 'math' changed from string to 90


# ------------------ ITERATION ------------------

print("All subjects and marks:")
for subject, value in marks.items():
    print(subject, ":", value)

# Output:
# english : 95
# chem : 98
# phy : 89
# math : 90
# maths : 99


# ------------------ BASIC INFO ------------------

print("Total subjects:", len(marks))
# Output: 5