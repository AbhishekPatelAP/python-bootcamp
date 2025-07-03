print("Hey Python")
print('Hi Python')

print("---------------------------------------")
print("             LEARN PYTHON              ")
print("---------------------------------------")
print("Hey \"Python\" ") # use of backslace
print('Hi "Python"') # we can use "" with '', if we want to print inything withing ""
print("path : C: user\\patel\\python") # use of \ to use in path

# print a scape new line using \n 
print("message 1\n")
print("message 2")

# OR
print("message 1 \n\nmessage 2")
print("Message 1\nMessage 2") # \n : used to scape to new line
print("Message 1\t Message 2") # \t : used to give a tab between two messages

# Question 1
# USE print to create this exect output
# you are allowed to use only print once
print("Your Learning Path :\n\t- Python Basic\n\t- Data Engineering\n\t- AI")

# OR
# we can use """ """, to separate the code as it is going to be in a big line
print("""Your Learning Path :
\t- Python Basic
\t- Data Engineering
\t- AI""")

# Basic message
print("Hello, world!")

# Concatenation with commas (automatic spaces)
name, score = "Alice", 92
print("User:", name, "| Score:", score)  # User: Alice | Score: 92

# No newline at the end
print("Loading...", end="")   # keeps cursor on same line

# Custom separator
print("a","b","c", sep="|")   # a|b|c

# Debug example
subtotal = 1200
discount = 0.15 * subtotal
final_total = subtotal - discount
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final total:", final_total)
