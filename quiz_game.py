print("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

# Question 1
answer = input(
    "What is the method called that's used to find the length of a list in Python? ")
if answer == "len":
    print("Correct!")
else:
    print("Incorrect!")

# Question 2
answer = input(
    "Which keyword is used to create a loop in Python? (Hint: There are two correct answers) ")
if answer == "for" or answer == "while":
    print("Correct!")
else:
    print("Incorrect!")

# Question 3
answer = input("What symbol is used to start a comment in Python? ")
if answer == "#":
    print("Correct!")
else:
    print("Incorrect!")

# Question 4
answer = input("Which function converts a string to a float in Python? ")
if answer == "float":
    print("Correct!")
else:
    print("Incorrect!")

# Question 5
answer = input("What does 'IDE' stand for in programming? ")
if answer == "Integrated Development Environment" or answer == "integrated development environment":
    print("Correct!")
else:
    print("Incorrect!")

# Question 6
answer = input(
    "Which data type would you use to store a sequence of characters in Python? ")
if answer == "string" or answer == "String":
    print("Correct!")
else:
    print("Incorrect!")

# Question 7
answer = input(
    "In Python, which operator is used for exponentiation (power calculation)? ")
if answer == "**":
    print("Correct!")
else:
    print("Incorrect!")

# Question 8
answer = input("What keyword in Python is used to define a function? ")
if answer == "def":
    print("Correct!")
else:
    print("Incorrect!")

# Question 9
answer = input(
    "What data type is the result of the expression 3 + 1.5 in Python? ")
if answer == "float" or answer == "Float":
    print("Correct!")
else:
    print("Incorrect!")

# Question 10
answer = input(
    "What do you call the error when your program tries to access an index that is out of bounds in a list? ")
if answer == "IndexError":
    print("Correct!")
else:
    print("Incorrect!")
