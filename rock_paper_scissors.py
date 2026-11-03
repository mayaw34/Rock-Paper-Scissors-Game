import random

player_name = input("Enter your name: ").strip()

if player_name == "":
    player_name = "Player"

player_score = 0
computer_score = 0
tie_score = 0

print("Hello, " + player_name + "!")
print("Type rock, paper, or scissors to play. Type quit to finish.")

while True:
    player_choice = input("Your choice: ").strip().lower()

    if player_choice == "quit":
        break
    elif player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
        computer_number = random.randint(1, 3)

        if computer_number == 1:
            computer_choice = "rock"
        elif computer_number == 2:
            computer_choice = "paper"
        else:
            computer_choice = "scissors"

        print("Computer chose " + computer_choice + ".")

        if player_choice == computer_choice:
            print("It's a tie!")
            tie_score = tie_score + 1
        elif player_choice == "rock" and computer_choice == "scissors":
            print(player_name + " wins this round!")
            player_score = player_score + 1
        elif player_choice == "paper" and computer_choice == "rock":
            print(player_name + " wins this round!")
            player_score = player_score + 1
        elif player_choice == "scissors" and computer_choice == "paper":
            print(player_name + " wins this round!")
            player_score = player_score + 1
        else:
            print("Computer wins this round!")
            computer_score = computer_score + 1

        print("Score: " + player_name + " " + str(player_score) + " - " + str(computer_score) + " Computer")
    else:
        print("Please enter rock, paper, scissors, or quit.")

print("Final score: " + player_name + " " + str(player_score) + " - " + str(computer_score) + " Computer")
print("Ties: " + str(tie_score))