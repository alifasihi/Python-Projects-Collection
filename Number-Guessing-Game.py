from random import randint

lower_num, upper_num = 1, 10

random_number: int = randint(lower_num, upper_num)

print(f'Guess the number in the range from {lower_num} to {upper_num}')

while True:
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Pleas enter a valid number')
        continue

    if user_guess > random_number:
        print("the number is lower")
    elif user_guess < random_number:
        print("the number is higher")
    else:
        print("the number is correct")
        break
