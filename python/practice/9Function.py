# ------------------ IMPORTING MODULE ------------------

import math              # Import full math module
from math import *      # Import all functions directly (not recommended in large programs)

# ------------------ VIEW AVAILABLE FUNCTIONS ------------------

print("Functions in math module:")
print(dir(math))
# Output: List of all available functions/constants in math module
# Example (partial):
# ['acos', 'asin', 'atan', 'ceil', 'cos', 'degrees', 'e', 'exp',
#  'fabs', 'factorial', 'floor', 'log', 'pi', 'pow', 'sin', 'sqrt', ...]

# ------------------ USING FUNCTIONS ------------------

print("Square root of 16:", sqrt(16))
# Output: 4.0


# ------------------ ADDITIONAL MATH FUNCTIONS ------------------

# Power
print("2^3:", pow(2, 3))
# Output: 8.0

# Ceiling (round up)
print("Ceil of 4.2:", math.ceil(4.2))
# Output: 5

# Floor (round down)
print("Floor of 4.8:", math.floor(4.8))
# Output: 4

# Factorial
print("Factorial of 5:", math.factorial(5))
# Output: 120

# Value of pi
print("Value of pi:", math.pi)
# Output: 3.141592653589793

# Logarithm (base e)
print("Log of 10:", math.log(10))
# Output: ~2.302585

# Trigonometric function
print("Sin(90° in radians):", math.sin(math.radians(90)))
# Output: 1.0


# ------------------ BEST PRACTICE NOTE ------------------

# Using: from math import *
# ❌ Not recommended in large programs (can overwrite names)

# Better:
# import math → use math.sqrt(), math.pi, etc.