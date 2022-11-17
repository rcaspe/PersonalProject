# Simple Quiz App
# Try

# Lets greet our visitor!
print("Welcome to this simple quiz app")

# Lets ask our vistor his/her name
x = input("What is your name: ")

# Lets verify if they want to proceed to the quiz
print("So, " + x + "! Would you like to proceed?")
y = input("").lower()

if y == "yes":
    print("Lets go!")

    # Lets proceed to the questions!
    print("Good Luck!")

    s = 0
    r = 0

    q1 = int(input("Question 1: 1 + 1 = "))
    if q1 == 2:
        s = s + 1
    else:
        r = r + 1

    q2 = int(input("Question 2: 1 + 1 = "))
    if q2 == 2:
        s = s + 1
    else:
        r = r + 1
    
    q3 = int(input("Question 3: 1 + 1 = "))
    if q3 == 2:
        s = s + 1
    else:
        r = r + 1
    
    q4 = int(input("Question 4: 1 + 1 = "))
    if q4 == 2:
        s = s + 1
    else:
        r = r + 1
    
    q5 = int(input("Question 5: 1 + 1 = "))
    if q5 == 2:
        s = s + 1
    else:
        r = r + 1

    print("You managed to get a ", s, "out of ", (s + r), "! points!")

else:
    print("Bye!")

if s >= 3:
    print("Congratulations! You didn't failed taking the easiest quiz ever!")
else:
    print("How come you failed that test??? Huh??")