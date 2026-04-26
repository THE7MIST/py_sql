# String Initialization
name = "aice Stack"

# Original String
print("Original:", name)  
# Output: aice Stack

# Case Conversions
print("Uppercase:", name.upper())  
# Output: AICE STACK

print("Lowercase:", name.lower())  
# Output: aice stack

print("Title Case:", name.title())  
# Output: Aice Stack

# Length of String
print("Length:", len(name))  
# Output: 10

# Finding Characters
print("Find 'S':", name.find('S'))  
# Output: 5

print("Find 's':", name.find('s'))  
# Output: -1

# Replace Substring
print("Replace 'ack' with 'anack':", name.replace("ack", "anack"))  
# Output: aice Stanack

# Membership Check
print("'st' in name:", "st" in name)  
# Output: False

print("'St' in name:", "St" in name)  
# Output: True


# ------------------ Additional String Functions ------------------

# Strip (removes spaces from start and end)
text = "  Hello World  "
print("Strip:", text.strip())  
# Output: Hello World

# Split (converts string to list)
print("Split:", name.split())  
# Output: ['aice', 'Stack']

# Join (joins list into string)
words = ['AI', 'is', 'powerful']
print("Join:", " ".join(words))  
# Output: AI is powerful

# Startswith & Endswith
print("Starts with 'a':", name.startswith('a'))  
# Output: True

print("Ends with 'k':", name.endswith('k'))  
# Output: True

# Count occurrences
print("Count of 'a':", name.count('a'))  
# Output: 2

# Swap case
print("Swapcase:", name.swapcase())  
# Output: AICE sTACK

# Capitalize (first letter uppercase)
print("Capitalize:", name.capitalize())  
# Output: Aice stack