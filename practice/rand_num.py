
import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    tries = 0

    while guess != random_number:
        tries += 1
        guess = int(input(f'Guess an number between 1 and {x}: '))
        if tries == 5:
            print(f'sry you loose!!! the number was {random_number}')
            break
        elif guess < random_number:
            print('sry, to low!')
        elif guess > random_number:
            print('sry, to high')

    print(f'You got it right!! {random_number}')


guess(20)
