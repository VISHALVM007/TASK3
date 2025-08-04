'''
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

sample_number = 5
result = factorial(sample_number)

print(f"The factorial of {sample_number} is: {result}")
'''

import math

number = float(input("Enter a number: "))

# Calculate results
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

# Display the results
print("Square root of", number, "is:", square_root)
print("Natural logarithm (log base e) of", number, "is:", natural_log)
print("Sine of", number, "(in radians) is:", sine_value)


