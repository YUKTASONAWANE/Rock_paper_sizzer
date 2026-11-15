import random


choices = ("rock", "paper", "scissors")

print("Rock, Paper, Scissors!")

while True:
    player = input("Choose rock, paper, scissors, or quit: ").strip().lower()

    if player == "quit":
        print("Thanks for playing!")
        break

    if player not in choices:
        print("Please enter rock, paper, scissors, or quit.")
        continue

    computer = random.choice(choices)
    print(f"You chose {player}. The computer chose {computer}.")

    if player == computer:
        print("It's a tie!")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("The computer wins!")