import random

user_wins = 0
computer_wins = 0
options = ["r", "p", "s"]

while True:
    user_input = input("Type R for Rock/P for Paper/S for scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("please enter a valid option for this game")
        continue
    random_number = random.randint(0, 2)
#    rock:0 paper:1 , scissors:2
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick} .")

    if user_input == "r" and computer_pick == "s":
        print("You won !")
        user_wins += 1

    elif user_input == "p" and computer_pick == "r":
        print("You won !")
        user_wins += 1

    elif user_input == "s" and computer_pick == "r":
        print("You won !")
        user_wins += 1
    else:
        print("you lost :-(")
        computer_wins += 1

print(f"You won {user_wins} times")
print(f"computer wins {computer_wins} times")
print("Good bye!! ")
