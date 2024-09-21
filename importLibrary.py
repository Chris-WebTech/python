# -*- coding: utf-8 -*-
"""
Christopher Miller
09/21/2023
04Assingment

# Hint
a = "Python"
    
print(a[0])
"""
import random
import sys
def q1():
   
    word = input("\nEnter a word: \n")
    # word = "python"
    
    # x = word[0]
    # print(x)
    
    y = len(word) - 1
    print(y)
    
    for y in range(y , -1 , -1):
        sys.stdout.write(word [y])
    print("\n\n")
    
def q2():
    a = 0
    
    for c in range(101):
        if( c % 3 == 0):
            # print(c)
            sys.stdout.write(str(c) + " ")
            a = a + 1
    print("\n\n")
    
    print("There are " + str(a) + " divisibal by three.")
    
    print("\n\n")
    
    # I did not know where to start on this one.
def lettercounter():
    # count letters, numbers, and symbols
    goodletters = 0
    baddletters = 0
    
    theWord = input("Enter the characters: ")
    print("\n\n")
    print("You entered " + theWord)
    print(chr(65))
    print(ord('A'))
    
    for l in theWord:
        # Turning letters into numbers
        ln = ord(l)
        if((ln >= 65 and ln <= 90) or (ln >= 97 and ln <= 122)):
            goodletters = goodletters + 1
        else:
            baddletters = baddletters + 1

    print("Good letters = " + str(goodletters) +
          "\nBad Letters = " + str(baddletters))
    
    print("\n\n")
def calendar():
    # 31 days & the user picks which day to start
    days = 31
    calendarday = 1
    startDay = int(input("Enter start Day"))
    
    days = days + startDay
    
    print("   S   M   T   W   T   F   S")
    
    for d in range(days):
        
        if(d % 7 == 0 and d > 0):
            print()
        
        if (d < startDay):
            sys.stdout.write(" ".rjust(4))
            
        else:
            sys.stdout.write(str(calendarday).rjust(4))
            
            calendarday = calendarday + 1
#-------------------------------------------------------#

# This is the idea I had in mind and the point of conflict came trying to 
# get the days to wrape accordingling.

#-------------------------------------------------------#
# def countBy():
#     mnu = """
#     # | Main Menu |
#     # 1. Sunday
#     # 2. Monday
#     # 3. Tuesday
#     # 4. Wednesday
#     # 5. Thursday
#     # 6. Friday
#     # 7. Saturday
#     # """
#     print(mnu)
#     choice = int(input("Enter 1 - 6: "))
    
#     if(choice == 1):
#         numStart = 1
#         numEnd = 32
#         numCols = 7
#         colcount = 0
    
#         numLen = len(str(numEnd)) + 2
        
        
#         print("   S   M   T   W   T   F   S")
#         for c in range(numStart,numEnd,):
            
#             sys.stdout.write(str(c).rjust(numLen, " "))
            
#             colcount = colcount + 1
#             # colcount += 1 (either work)
#             if(colcount >= numCols):
#                 print()
#                 colcount = 0
#     elif (choice == 2):
#         numStart = 1
#         numEnd = 32
#         numCols = 7
#         colcount = 0
    
#         numLen = len(str(numEnd)) + 2
        
        
#         print("   S   M   T   W   T   F   S")
#         for c in range(numStart,numEnd,):
            
#             sys.stdout.write(str(c).rjust(numLen, " "))
            
#             colcount = colcount + 1
#             # colcount += 1 (either work)
#             if(colcount >= numCols):
#                 print()
#                 colcount = 2
# """


def grida():
    print("Q5a")

    nc = 0
    nr = 10
    
    for r in range(nr):
        for c in range (nc):
            sys.stdout.write("*")
        print()
        
        nc = nc + 1
        

    print("Q5b")

    nc = 10
    nr = 10

    # the number of rows
    for r in range(nr):

        # this is a row (prints the columns)

        for c in range(nc):
            sys.stdout.write("*")
        print()

        nc = nc - 1
        

    print("Q5c")

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

    print("Q5d")

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
        

    print("Q5e")

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
    print("\nGreetings to pick a number game.\n")
    re = random.randint(1,101)
    guessAgain = "y"
    # for c in range():
    while(guessAgain == "y"):
        
        imput = int(input("Guess a Number"))

    # I couldn't figure out how to keep track of the guesses\
    # My first hunch was a for statment with c tracking the number of guesses
    # ---this will be if statement going up or down

        if(imput == re):
            print("\nYou Guessed Right: \n" + str(re) + " Took you: ")
            guessAgain = input("Would you like to guess again? y = yes | n = n").lower()
            re = random.randint(1,101)
            
        elif(imput > re):
            print("\nYou guessed high: \n")
            
        elif(imput < re):
            print("\nYou guessed low\n")
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
        

def main():
    
    # q1()
    # q2()
    # grida()
    # print("\n\n")
    # numPick()
    # menu1()
        
    print("\n")
    
    quit = "n"
    
    while(quit != "y"):
        menu1()
        quit = input("Would you like to quit? y/n")
        
    print("\nBye")
    

main()


"""
Loop Exercise – Rev 2 
for counter in range(start,stop,countby):
 # your code goes here
1. 5 pts - Write a function that will allow the user to enter a word, then 
using a loop (hint a for statement), print the word in reverse. Use 
sys.stdout.print() statement. 
HINT: len()
2. 5 pts - Write a function that will count all of the numbers divisible by 3 
for the set 1 - 100.
HINT - remainder
3. 5 pts Write a function that will allow the user to enter a word with upper 
case, lower case, and numbers and symbols. Count the following good letters 
(upper and lower case only), bad letters - (any other symbol or numbers). DO 
NOT USE THE COMMAND "SEARCH". For instance Aa2#4bD has four good letters and 2 
bad letters.
HINT - run the following code and use the ASCII table. You will need to loop 
and IF you think about the problem, it will be easy IF you get my drIFt.
 # run this first and observe the output
 print(chr(66))
 print(ord('A'))
4. 5 pts - Calendar Shift
Write a program that does the following: (User gets to enter how many 
positions to shift to the right (1 - 6)) You must use a loop(s). IF you think 
about the problem, it will be easy IF you get my drIFt. 
HINT: max iterations
Enter the number of positions to shift: 4
Output: 
S M T W R F S
 1 2 3 
4 5 6 7 8 9 10 
11 12 13 14 15 16 17 
18 19 20 21 22 23 24 
25 26 27 28 29 30 3
"""