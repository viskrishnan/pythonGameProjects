print("Welcome to Quiz Game")

playing = input("Do you want to play a game ? ")

if playing.upper() != "YES":
    quit()

print("Okay ! Lets play the game !")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct Answer!!")
else:
    print("Incorrect Answer!")
