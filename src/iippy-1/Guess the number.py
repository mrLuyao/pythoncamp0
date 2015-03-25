# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

#init global vari

secret_number = 0
range_number = 100
your_guess_number = 0
chance_number = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randint(0, range_number)
    print 'A new game was started.Pleass guess a number.'
    print 'The range is 0 to',range_number,'.'
    print 'secret_number is',secret_number

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_number
    global chance_number
    chance_number = 7
    range_number = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global range_number
    global chance_number
    chance_number = 7
    range_number = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global chance_number
    your_guess_number = int(guess)
    print 'you guess it is',your_guess_number
    chance_number = chance_number - 1
    if chance_number == 0 and your_guess_number != secret_number:
        print 'You should learn dichotomy.'
        range100()
    elif your_guess_number == secret_number:
        print 'Correct!','The secret number is',secret_number
    elif your_guess_number > range_number:
        print 'You fool,your guess number is out of the range'
        print 'Your chance left',chance_number
    elif your_guess_number > secret_number:
        print 'Guess too high'
        print 'Your chance left',chance_number
    elif your_guess_number < secret_number:
        print 'Guess too low'
        print 'Your chance left',chance_number
    else:
        print 'input error'
        print 'Your chance left',chance_number
        

    
# create frame
f = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
f.add_button('A new game from 0 to 100',range100,200 )
f.add_button('A new game from 0 to 1000',range1000,200 )
f.add_input('Enter a guess',input_guess,200)


# call new_game 
range100()


# always remember to check your completed program 
# against the grading rubric