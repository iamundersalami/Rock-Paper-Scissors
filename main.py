import random

list = ['rock', 'paper', 'scissors']


def main():
    def loose():
        print("You loose")
    player = input("============================================="
                   "\nEnter: rock, paper or scissors: ")
    if player not in list:
        print("Error")
    else:
        computer = random.choice(list)
        print(f'You: {player}\nComputer: {computer}')
        if player == computer:
            print('draw')
        elif player == 'rock' and computer == 'paper' \
                or player == 'paper' and computer == 'scissors' \
                or player == 'scissors' and computer == 'rock':
            loose()
        else:
            print('You won')


while True:
    main()
