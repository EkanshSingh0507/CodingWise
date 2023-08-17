import random
options= ["rock","paper","scissors"]

computer_choice = random.choice(options)
user_choice = input("Enter your guess = ").lower()

if user_choice == "paper" and computer_choice == "rock":
    print("You Won")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You Won")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You Won")
elif user_choice == computer_choice:
    print("Tied")
else:
    print(f"You lost, computer's choice was {computer_choice}")