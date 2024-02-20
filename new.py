import time

#First we create a list with 4 integers.
guess_list = [32,45,56,76]

"""This function checks if the value given py the player is in the list. If it is in the list, 
it prints a success message. Otherwise it prints fail message"""
def guessFunction(value):
    if value in guess_list:
        print("The value guessed is in the list")
        popFunction(value)
    else:
        print("The value guessed is not in the list")

#This function removes the guessed value from the list and the remaining list becomes the new list 
def popFunction(value):
    guess_list.remove(value)

#This function checks the length of the list. If the list has no remaining values (is empty). The player has won the game and the game exits
"""def gameWin():
    list_length = len(guess_list)
    print(f"There are {list_length} numbers in the list.")
    if list_length <= 0:
        print("You have guessed all the numbers in the list")
        prompt2 = input("Do you want to play again? (Y/N)").capitalize()
        if prompt2 == "Y":
            main()
        else:
            print("Goodbye player 1")
            time.sleep()
            return None
"""
        
"""This is the main function of the game. First it sets a flag, isActive as True. This flag will be used to check whether the player wants to exit the game or continue playing. 
When the flag is True, the game asks for an input from the player. If the value is 0 (value == 0), the flag is set to False and the game should exit. When the player gives another
number, the game calls the guessFunction function and uses the value as input. The function runs and then returns to the point where it asks for the players input"""
def main():
    print("Welcome to the guessing game")
    isActive = True
    while isActive != False:
        value = int(input("Guess a number (0 to quit): "))
        if value == 0:
            isActive = False
            prompt = input("Do you want to quit?(Y/N) ").capitalize()
            if prompt == "Y":
                print("Goodbye")
                time.sleep(3)
                return None
            else:
                main()
        else:
            guessFunction(value)

main()
#Tasks:1) figure out the gameWin() function 2) use rich text to make it more appealing 3) upload to github