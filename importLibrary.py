# -*- coding: utf-8 -*-
"""
Christopher Miller
09/21/2023

For Loops:
    | Main Menu |
    1. Display a Word backwards
    2. Numbers divisibal by Three
    3. Password Genorator
    4. Calendar
    5. (*) Grids
    6. Guess a Number
"""
# import random for random number generator
import random
# Import sys python interpreter 
import sys

# user enters word, program loops it backrwards
def q1():
   
   # user word
    word = input("\nEnter a word: \n")
    
    # length of the word
    # -1 because python starts at 0
    y = len(word) - 1
    
    # Loop for y (length of word)
    for y in range(y , -1 , -1):

        # y eaquals each letter
        sys.stdout.write(word [y])

    print("\n\n") # Spacer
    
# program calculates how many numbers are
# divisable by 3 in 100
def q2():

    # Answer Defualt = 0
    a = 0
    
    # for each c in 100 equals a good answer
    for c in range(101):

        # if answer is good
        if( c % 3 == 0):
            sys.stdout.write(str(c) + " ")

            # another number added to answer
            a = a + 1
    print("\n\n")
    
    # display answer
    print("There are " + str(a) + " divisibal by three.")
    
    print("\n\n")


def lettercounter():
    # count letters, numbers, and symbols
    goodletters = 0
    baddletters = 0
    
    # user enters word
    theWord = input("Enter the characters: ")
    print("\n\n")
    print("You entered " + theWord)
    
    # loop through each letter
    for l in theWord:
        # Turning letters into numbers
        ln = ord(l)

        # ascii table values
        if((ln >= 65 and ln <= 90) or (ln >= 97 and ln <= 122)):
            goodletters = goodletters + 1
        else:
            baddletters = baddletters + 1

    print("Good letters = " + str(goodletters) +
          "\nBad Letters = " + str(baddletters))
    
    print("\n\n")

# display a 31 day calendar
def calendar():
    # 31 days
    days = 31
    calendarday = 1
    # User picks which day to start
    startDay = int(input("Enter start Day"))
    
    days = days + startDay
    
    print("   S   M   T   W   T   F   S")
    
    # Loop user input days
    for d in range(days):
        
        if(d % 7 == 0 and d > 0):
            print()
        
        if (d < startDay):
            # rjust ads "right padding"
            sys.stdout.write(" ".rjust(4))
            
        else:
            sys.stdout.write(str(calendarday).rjust(4))
            
            calendarday = calendarday + 1

# Display *
def grida():

    nc = 0
    nr = 10
    
    for r in range(nr):
        for c in range (nc):
            sys.stdout.write("*")
        print()
        
        nc = nc + 1
# --------------------
    nc = 10
    nr = 10

    # the number of rows
    for r in range(nr):

        # this is a row (prints the columns)
        for c in range(nc):
            sys.stdout.write("*")
        print()

        nc = nc - 1
# --------------------
    nc = 10
    nr = 10
    ncc = 0
    # the number of rows
    for r in range(nr):

        # this is a row (prints the columns)
        for c in range(ncc):
            sys.stdout.write(" ")
        for c in range(nc):
            sys.stdout.write("*")

        print()

        ncc = ncc + 1
        nc = nc - 1
# --------------------
    nc = 0
    nr = 10
    ncc = 10

    # the number of rows
    for r in range(nr):

        # this is a row (prints the columns)

        for c in range(ncc):
            sys.stdout.write(" ")
        for c in range(nc):
            sys.stdout.write("*")


        print()

        ncc = ncc - 1
        nc = nc + 1
        

# --------------------

    nc = 0
    nr = 7
    ncc = 7
    nC = 7
    Nc = 0
    for r in range (nr):

        for c in range(nc):
            sys.stdout.write(" ")
        for c in range(ncc):
            sys.stdout.write("*")
        for c in range(nC):
            sys.stdout.write("*")
        for c in range(Nc):
            sys.stdout.write(" ")

        print()
        Nc = Nc + 1
        nC = nC - 1
        ncc = ncc - 1
        nc = nc + 1
        
# --------------------

    nc = 0
    nr = 8
    ncc = 7
    nC = 7
    Nc = 0
    # for r in range(nr):



    # the number of rows


    for r in range (nr):
        for c in range(nC):
            sys.stdout.write(" ")
        for c in range(Nc):
            sys.stdout.write("*")
        # this is a row (prints the columns)
        for c in range(nc):
            sys.stdout.write("*")
        for c in range(ncc):
            sys.stdout.write(" ")



        print()
        Nc = Nc + 1
        nC = nC - 1
        ncc = ncc - 1
        nc = nc + 1
    

def numPick():
    print("\Welcome to pick a number game.\n")

    # generate a random number between 1-100
    re = random.randint(1,101)

    guessAgain = "y"

    # while player wants to play
    while(guessAgain == "y"):
        
        # player guesses
        imput = int(input("Guess a Number"))

        # If player guesses right
        if(imput == re):
            print("\nYou Guessed Right: \n" + str(re) + " Took you: ")
            guessAgain = input("Would you like to guess again? y = yes | n = n").lower()
            re = random.randint(1,101)
        # player guesses high
        elif(imput > re):
            print("\nYou guessed high: \n")
        # player guesses low
        elif(imput < re):
            print("\nYou guessed low\n")

# Main menu - if menu
def menu1():
    mnu = """
    | Main Menu |
    1. Enter a Word backwards
    2. Numbers divisibal by Three
    3. Password Genorator
    4. Calendar
    5. (*) Grids
    6. Guess a Number
    """
    print(mnu)
    
    choice = int(input("Enter 1 - 6: "))
    
    if(choice == 1):
        q1()
        
    elif(choice == 2):
        q2()
        
    elif(choice == 3):
        lettercounter()
        
    elif(choice == 4):
        calendar()
        print("\n")
        
    elif(choice == 5):
        grida()
        
    elif(choice == 6):
        numPick()
        
# Run main program
def main():
        
    print("\n")
    
    quit = "n"
    
    while(quit != "y"):
        menu1()
        quit = input("Would you like to quit? y/n")
        
    print("\nBye")
    
main()