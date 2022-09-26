import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def main():
    player1 = input("Player 1, Enter your name: ")
    player2 = input("Player 2, Enter your name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled a', roll1)
    print(player2, 'rolled a', roll2)

    if roll1 > roll2:
        print(player1, 'won')
    elif roll1 == roll2:
        print('tie')
    else:
        print(player2, 'won')

main()