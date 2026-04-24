import random

options=[ "rock","paper","scissors"]
player_score=0
computer_score=0

print("welcome to the game! the first one to reach 3 wins.")

while player_score < 3 and computer_score < 3:
    computer_choice = random.choice(options)
    user_choice = input("\n make your move (rock, paper, scissors):").lower().strip()

    if user_choice not in options:
        print("invalid move! try again")
        continue
    print(f"computer_selection: {computer_choice}")

    if user_choice == computer_choice:
       print("scoreless")

    elif (user_choice == "rock") and (computer_choice == "scissors") or \
         (user_choice == "paper") and (computer_choice == "rock") or \
         (user_choice == "scissors") and (computer_choice == "paper") :
        print("you won")
        player_score += 1

    else:
        print("computer won")
        computer_score += 1
    print(f"score -> you : {player_score} |computer:{computer_score}")

if player_score == 3:
   print("congratulations, you won!")
else:
   print("unfortunately the computer won!")

