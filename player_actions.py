#Estephania Martinez  02/01/21
#player_actions.py
#Will ask player for input to decide if they want to play again
#options are 'Y' for yes., play again' and
#'N' for no, 'no, quit the game'
#If anything is entered the program will say "invalid input' and
#proceed to ask again



def check_play_again(user_input):
    #If the user input is 'Y' the program will print out 'Yes, play again'
    if user_input == 'Y': 
                print("Yes, play again")
    #If the user inputs 'N' the program will prin out 'N. quit the game'
    elif user_input == 'N':
                print("No, quit the game")
    #If the user enters anything other than 'Y' or 'N' the output will be 'Invald input'
    #This includes 'y' and 'n'
    else:
                print("Invalid input")
                         
    #Your code here


check_play_again(input("Would you like to play again? Type 'Y' for Yes or 'N' for No: \n"))

