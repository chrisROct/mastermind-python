#! sys/bin/python3

from random import randint
import sys

# method to clear space for better readability.
def clear(n):
    for i in range(n):
        print()
# this method creates three lists. a randomized list, a list for storing user guesses
# and a third list to validate guesses against..       
def mastermind():
    mastermindCombination = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
    guessCombination = [int(), int(), int(), int()]
    GameIsOver = False
    guesses = 0
    
    while GameIsOver == False:
        checker=["", "", "", ""]
        rightval = 0 
        rightpos = 0
        
        if guesses >= 10:
            GameIsOver = True
            clear(5)
            print("Mastermind has bested you! Better luck next time!")
            menu()
        else:
            awaitingInput = True
            while awaitingInput:
                try:
                    for l in range(0, len(mastermindCombination)):
                        guessCombination[l] = int(input(f"Choose an integer from 1 to 6 to put in position {l+1}/4: "))
                    for k in range(0,len(guessCombination)):
                        if ((int(guessCombination[k]) >6 or int(guessCombination[k]) <1)):
                                clear(2)
                                raise ValueError()
                except ValueError:
                    clear(2)
                    print("Invalid Input. Please choose an integer from 1 to 6.")
                else:
                    awaitingInput = False
            guesses += 1
            if mastermindCombination == guessCombination:
                GameIsOver = True
                clear(5)
                print("Mastermind is no match for you! You have earned bragging rights!")
                print(f"The winning combination was: {mastermindCombination}\nYou won using {guesses} guesses.")
                menu()
            else:           
                for i in range(0,len(mastermindCombination)):
                    for j in range(0,len(guessCombination)):
                        if guessCombination[j] == mastermindCombination[j]:
                            checker[j] = "pos"
                            rightpos = checker.count("pos")
                        elif guessCombination[j] == mastermindCombination[i]:
                            if checker[i] == "":
                                checker[i] = "val"
                                rightval = checker.count("val")
                                
                clear(2)
                print(f"number of guesses in total: {guesses} out of 10")
                print(f"so far you've guessed {rightval} correct values in the wrong position")
                print(f"and you've guessed {rightpos} correct values in the right position.")
                clear(2)
                print(f"your last guess was: {guessCombination}")
def rules():
    print("--WELCOME TO MASTERMIND--\n--Rules--\nIn this Game you receive an invisible List with 4 items.\nEach item has a value from 1 to 6. And you get 10 combination guesses\n10 Guesses to pinpoint the correct combination of hidden values stored in the List\n\n--Controls--\nAll Input is given via Keyboard. 'P', 'Q', 'R', and 'Enter' navigate the Menu\n Valid Input for Mastermind are the Digits '1-6' and 'Enter'.\nOn the rules screen, you can use the any key.")
    clear(2)
    print("Press any key followed by 'Enter' to return to the menu")
    playerInput = input()
    if playerInput != "":
        clear(10)
        menu()
    else:
        clear(10)
        menu()

# could have used match cases here, but with only three options, an if-elif-else function seemed appropriate.
def menu():
    clear(2)
    print("--MENU--")
    print("'P' to Play")
    print("'Q' to Quit")
    print("'R' for Rules")
    print("Press 'Enter' to confirm.")
    playerInput = input("input:")
    if playerInput == 'p':
        clear(10)
        print("Starting Match!")
        mastermind()
    elif playerInput == 'r':
        clear(10)
        rules()
    elif playerInput == 'q':
        print("Quitting...")
        sys.exit()
    else:
        clear(3)
        print("no.")
        clear(7)
        menu()
        
if __name__ == "__main__":
    menu()