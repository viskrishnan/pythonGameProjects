print("Welcome to Quiz Game")

playing = input("Do you want to play a game ? ")

if playing.upper() != "YES":
    quit()

print("Okay ! Lets play the game !")
score = 0

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct Answer!!")
    score += 1
else:
    print("Incorrect Answer!")

answer = input("What does GPU stand for? ")
if answer == "graphical processing unit":
    print("Correct Answer!!")
    score += 1
else:
    print("Incorrect Answer!")

print(f"You scored {score} points !!")


