import datetime


def getdate():
    return datetime.datetime.now()


print('HEALTH MANAGEMENT SYSTEM')
dict1 = {1: 'Shahid', 2: 'Azeem', 3: 'Hassan'}
client_no = int(input('Client No (1 for Shahid, 2 for Azeem, 3 for Hassan): '))
person = dict1.get(client_no)
choice_type = int(input('Write data (press 1) or Retrieve data (press 2)? '))
choice = int(input('Are you interested in Diet (press 1) or workout routine files (press 2)? '))

if choice_type == 1:
    if choice == 1:
        while True:
            input_diet = input('Enter your input: ')
            with open(f'{person}-diet.txt', 'a') as file:
                file.write(f'{str(getdate())} {input_diet} \n')
            reentry = input('Do you want to make another entry? (Y/N)')
            if reentry.lower() == 'n':
                break
    elif choice == 2:
        while True:
            input_workout = input('Enter your input: ')
            with open(f'{person}-workout.txt', 'a') as file:
                file.write(f'{str(getdate())} {input_workout} \n')
            reentry = input('Do you want to make another entry? (Y/N)')
            if reentry.lower() == 'n':
                break
elif choice_type == 2:
    if choice == 1:
        with open(f'{person}-diet.txt') as file:
            content = file.read()
            print(content)
    elif choice == 2:
        with open(f'{person}-workout.txt') as file:
            content = file.read()
            print(content)
