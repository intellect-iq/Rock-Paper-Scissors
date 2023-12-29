import random
computer_choice = ''


name = input("Enter your name: ")
print(f"Hello, {name}")
rating = 0

with open('rating.txt', 'r') as my_file:
    for line in my_file:
        if line.startswith(f'{name} '):
            rating = int(line.strip(f'{name} '))

default_choices = ["rock", "paper", "scissors"]
choices = input().split(sep=',')
if choices == ['']:
    choices = default_choices
indices = int((len(choices) - 1) / 2)

print("Okay, let's start")


def win():
    global rating
    print(f"Well done. The computer chose {computer_choice} and failed")
    rating += 100


def lose():
    print(f"Sorry, but the computer chose {computer_choice}")


def player(choice):
    global rating
    global computer_choice
    computer_choice = random.choice(choices)
    indices = int((len(choices) - 1) / 2)
    winningPosition = []
    losingPosition = []

    if choices.index(choice) == indices:
        losingPosition = choices[:indices]
        winningPosition = choices[indices + 1:]
    elif choices.index(choice) > indices:
        losingPosition = choices[choices.index(choice) - indices:choices.index(choice)]
        for x in choices:
            if x == choice:
                continue
            if x not in losingPosition:
                winningPosition.append(x)
    elif choices.index(choice) < indices:
        winningPosition = choices[choices.index(choice) + 1:choices.index(choice) + indices + 1]
        for x in choices:
            if x == choice:
                continue
            if x not in winningPosition:
                losingPosition.append(x)
    if computer_choice == choice:
        print(f"There is a draw ({computer_choice})")
        rating += 50
    elif computer_choice in winningPosition:
        lose()
    elif computer_choice in losingPosition:
        win()


while True:
    player_choice = input()
    if player_choice == "!exit":
        print("Buy!")
        break
    elif player_choice == "!rating":
        print(f"Your rating: {rating}")
        continue
    elif player_choice not in choices:
        print("Invalid input")
    else:
        player(player_choice)
