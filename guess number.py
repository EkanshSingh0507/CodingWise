import random

secret_number= random.randint(1,10)
user_number= int(input("Enter your number"))

if secret_number == user_number:
    print("You Won")
else:
    print(f"You Lost, the number was {secret_number}")