import random
while True:
    choice = input('Roll the dice? (y/n): ')
    if choice == 'y' or choice == 'Y':
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(f'{dice1}, {dice2}')

    elif choice == 'n' or choice == 'N':
        print('Thanks for playing!')
        break

    else:
        print('Invalid choice.')