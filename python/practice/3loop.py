# ------------------ WHILE LOOP (FLOAT INCREMENT) ------------------

i = 3

# Loop runs while i <= 10, incrementing by 1.5
while i <= 10:
    print(i)
    i += 1.5

# Output:
# 3
# 4.5
# 6.0
# 7.5
# 9.0
# 10.5   (last value printed because condition checked before increment)


# ------------------ WHILE LOOP (PATTERN PRINTING) ------------------

i = 1

# Prints increasing number of '#' symbols
while i <= 10:
    print(i * "#")
    i += 1

# Output:
# #
# ##
# ###
# ####
# #####
# ######
# #######
# ########
# #########
# ##########


# ------------------ FOR LOOP WITH RANGE ------------------

# Loop from 9 to 4 (reverse order)
for item in range(9, 3, -1):
    print(item)

# Output:
# 9
# 8
# 7
# 6
# 5
# 4


# ------------------ ADDITIONAL LOOP EXAMPLES ------------------

# 1. While loop with break
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1

# Output:
# 1 2 3 4 5


# 2. While loop with continue (skip even numbers)
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# Output:
# 1 3 5 7 9


# 3. For loop with enumerate
fruits = ["apple", "banana", "cherry"]

for index, value in enumerate(fruits):
    print(index, value)

# Output:
# 0 apple
# 1 banana
# 2 cherry


# 4. Nested loop (simple pattern)
for i in range(1, 4):
    for j in range(i):
        print("*", end="")
    print()

# Output:
# *
# **
# ***


# 5. Sum using loop
total = 0
for i in range(1, 6):
    total += i

print("Sum:", total)

# Output:
# Sum: 15