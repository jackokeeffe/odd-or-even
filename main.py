def start_game():
    input_number()
    check_number()

def input_number():
    global number
    number = int(input('Enter a number and I will tell you if it is odd or even: '))

def check_number():
    global number
    if number % 2 == 0:
       even_output()
    elif number % 1 == 0:
        odd_output()
    elif number == 1:
        odd_output()

def even_output():
    play_again = input('That number is even! Play again? (y/n): ')
    if play_again == "y":
        start_game()
    elif play_again == "n":
        exit()
    else:
        print('Please enter a valid entry, (y = yes, n = no)!')
        check_number()

def odd_output():
    play_again = input('That number is odd! Play again? (y/n): ')
    if play_again == "y":
        start_game()
    elif play_again == "n":
        exit()
    else:
        print('Please enter a valid entry, (y = yes, n = no)!')
        check_number()

start_game()
