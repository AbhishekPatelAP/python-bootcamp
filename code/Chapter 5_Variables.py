# ================================================================================
# VARIABLES 
# ----------------------------------------
# Variables act as named containers for storing data in Python.
# You give a variable a value using the assignment operator `=`, then
# you can reuse that name throughout your code. We’ll also use
# the `print()` function to display both literals and variables.
# ================================================================================

# ---------------------------------------
# Without Variables
# ---------------------------------------
# Here we print fixed text directly using print().
print("My name is Abhishek")
print("Abhishek is learning Python")
print("Abhishek wants to become Python expert")

# ---------------------------------------
# Single Variable
# ---------------------------------------
# Store your name in a variable and reuse it in print().
name = "Abhishek"
print("My name is", name)
print(name, "is learning Python")
print(name, "wants to become Python expert")

# ---------------------------------------
# Multiple Variables
# ---------------------------------------
# Now we’ll keep both your name and the language in variables.
name     = "Abhishek"
language = "python"
print("My name is", name)
print(name, "is learning", language)
print(name, "wants to become", language, "expert")

# ---------------------------------------
# Python Challenge
# ---------------------------------------
# Print the following three lines:
#     info@connect_patel.com
#     support@connect_patel.com
#     www.connect_patel.com
# Use a variable for the base domain to make it dynamic!

domain = "connect_patel.com"
print("info@" + domain)
print("suppost@" + domain)
print("www." + domain)