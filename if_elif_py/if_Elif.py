# -*- coding: utf-8 -*-
"""
09/26/23
Christopher Miller

if/elif Menu, Calulator and Game.

"""
def playGame():
    print("Your a miner and the cave just collapsed. to survive " +
            "you move around sorting the tunel for equipment. Your first"
            + " choice comes when you come across a shovel and a Torch")

    print("Do you pick the; 1 = shovel, or 2 = Torch?")
    
    choice = input("enter 1 or 2: ")
    print("\n")

    if(choice == "1"):
        
        # left side
        print("\nYou picked the shovel! Allowing you to dig your way twards" 
              "the escape.\n")
        print("You dig to another portion of the cave and find a small "
              "opening and fresh air reasuing you servival. You know have two"
              "Options:\n 1) Turn around and help anyone else in the cave.\n"
              "2) leave and Find cell Service.")
        print("\nType: 1/2")
        
        # user gets two choises
        choice = input("enter 1 or 2: ")
        print("\n")
        
        # if user input is 1
        if(choice == "1"):
            print("\nBOOOM!\n")
            print("some idiot droped a torch in the TNT room collapsing"
                  " the entire cave")
            
            print("Thanks For Playing")

        # if user input is 2
        elif(choice == "2"):
            print("As you finally make it to sell serise and report what"
                  " happened the road gives from under you and you"
                  " are severly injurd due to someone Setting off the TNT"
                  " room in the Cave\n\n")
            print("was this fun; y = yes, or n = no")
           
            choice = input("enter y or n: ").lower()
            print("\n")
            
            if(choice == "y"):
                print("Your Awesome! Thanks for Playing.")
                print("\nBye")
    
            elif(choice == "n"):
                print("Make a better one?")
                print("\nBye")
            
    elif(choice == "2"):
        print("You chose a torch and continue exploring the rest of the cave")
        print("the easy option led you to the room full of T.N.T."
              "Staring at death do you turn and run or through the "
              "torch in the room\n")
        print("Option 1 = run")
        print("Option 2 = BOOM!")
        
        choice = input("Enter 1/2: ")
        
        if(choice == "1"):
            print("you turn and run bumping a powder caig setting off a chain"
                  "reaction colabsing East Denver")
        elif(choice == "2"):
            print("BOOOOOOOOOM")
            
            print("\nWas That fun?")
            choice = input("enter y or n: ").lower()
            print("\n")
            
            if(choice == "y"):
                print("Your Awesome! Thanks for Playing.")
                print("\nBye")
    
            elif(choice == "n"):
                print("Make a better one?")
                print("\nBye")
        else:
            return
    # if user inputs anything else
    else:
        print("That wasn't a choice - good bye")
        return     
    
    #--------------- Calculator -----------------#
def cal1(sAlary):

    if(sAlary > 0 and sAlary <= 9275):
        ans = sAlary / 10
        ans = round(ans,2)
        # print(str(ans))
        print("\nYou Pay $" + str(ans) +
              " in the 10% rate.")
        

    elif(sAlary > 9275 and sAlary <= 37650):
        ans = sAlary / 18
        ans = round(ans,2)
        # print(str(ans))
        print("\nYou Pay $" + str(ans) +
              " in the 18% rate.")
    
    
    elif(sAlary > 37650 and sAlary <= 91150):
        ans = sAlary / 25
        ans = round(ans,2)
        # print(str(ans))
        print("\nYou Pay $" + str(ans) +
              " in the 25% rate.")
    elif(sAlary > 91150 and sAlary <= 190150):
        ans = sAlary / 28
        ans = round(ans,2)
        print("\nYou Pay $" + str(ans) +
              " in the 28% rate.")
        
    elif(sAlary > 190150 and sAlary <= 413350):
        ans = sAlary / 33
        ans = round(ans,2)
        print("\nYou Pay $" + str(ans) +
              " in the 33% rate.")
        
    elif(sAlary > 413350 and sAlary <= 415050):
        ans = sAlary / 35
        ans = round(ans,2)
        print("\nYou Pay $" + str(ans) +
              " in the 35% rate.")
        
    elif(sAlary > 415050 and sAlary <= 415050 * 415050):
        ans = sAlary / 39.6
        ans = round(ans,2)
        print("\nYou Pay $" + str(ans) +
              " in the 39.6% rate.")
    
    # I understand I could do else: statement here as well
    elif(sAlary > 415050 * 415050 and sAlary <= 415050415050 *
         415050 * 415050415050415050):
        ans = sAlary / 39.6
        ans = round(ans,2)
        # print(str(ans))
        print("\nYou Pay $" + str(ans) +
              " and my cash app is WASPOPPIN... PLEASE")

def menu1():
    mnu = """
    This programe offers A game, Option: 1 
    and  a Tax Break Calculator, Option: 2
    1. Cave Collapse (Game)
    2. Tax Calculator (Calculator)
    """
    print(mnu)
    
    choice = int(input("Enter 1 / 2: "))
    
    # You can run an if statement in main
    if(choice == 1):
        playGame()
        
    elif(choice == 2):
        anum = int(input("Enter your salary: "))
        cal1(anum)
        1
    else:
        print("*Error*")
        

# Run main Program
def main():
        
    print("\n")
    
    quit = "n"
    
    # if quit does NOT equal Y
    # Program continues at menu1
    while(quit != "y"):
        menu1()
        quit = input("Would you like to quit? y/n")
        
    print("\nBye")
    
main()
