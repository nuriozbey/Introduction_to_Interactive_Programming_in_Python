# template for "Guess the number" mini-project-2
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
secret_num = 0
guesses_left = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    global secret_num
    global guesses_left
    
    secret_num = random.randrange(0, num_range)
    if num_range == 100 : 	
        guesses_left = 7
    elif num_range == 1000 :
        guesses_left = 10
      

    print "New game. The range is from 0 to", num_range, ". Good luck!"
    print "Number of remaining guesses is ", guesses_left, "\n"
   
    # remove this when you add your code    
    #pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100 
    new_game() 
    # remove this when you add your code    
    #pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000 
    new_game()
    pass
    
def input_guess(guess):
    # main game logic goes here	
    global guesses_left
    global secret_num 
    
    won = False
    
    print "You guessed: ",guess
    guesses_left = guesses_left - 1
    print "Number of remaining guesses is ", guesses_left
    
    if int(guess) == secret_num:       
        won = True
    elif int(guess) > secret_num:
        result = "Lower!"
    else:
        result = "Higher!"                
        
        
    if won:
        print "That is correct! Congratulations!\n"
        new_game()
        return
    elif guesses_left == 0:
        print "Game over. You didn't guess the number in time!"  
        print "secret num was", secret_num,"\n"
        new_game()
        return
    else:
        print result
    # remove this when you add your code
    #pass

    
# create frame
frame = simplegui.create_frame("Game: Guess the number!", 300, 300)
frame.set_canvas_background('Green')

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 150)
frame.add_button("Range is [0, 1000)", range1000, 150)	
frame.add_input("Enter your guess", input_guess, 150)

# call new_game 
new_game()
# start frame
frame.start()
# always remember to check your completed program against the grading rubric
