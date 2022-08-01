import random
option = ['Snake', 'Water', 'Gun']
random_var = random.choice(option)

while True:
    user_choice = input("Choose b/w 'Snake', 'Water' & 'Gun'. ")
    if user_choice.lower() == 'snake' and random_var.lower() == 'water':
        print('You win.')
    elif user_choice.lower() == 'water' and random_var.lower() == 'gun':
        print('You win.')
    elif user_choice.lower() == 'gun' and random_var.lower() == 'snake':
        print('You win.')
    else:
        print('You lose.')
    count = input('Want to try again? (Y/N) ')
    if count.lower() != 'y':
        print('See you next time.')
        break
    else:
        random_var = random.choice(option)