def guessing_game():
    from random import randint
    
    rand_int = randint(1, 100)
    
    while True:
            user_guess = int(input('Guess the number from 1 to 100: ').strip())
                        
            if rand_int == user_guess:
                print(f'You are right. You have correctly guessed number {rand_int} !')
                break
            elif rand_int < user_guess:
                print(f'The number you are looking for is lower than {user_guess}')
            else:
                print(f'The number you are looking for is higher than {user_guess}')
