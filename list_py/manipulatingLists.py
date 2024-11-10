# -*- coding: utf-8 -*-
"""
Christopher Miller
09/19/2023
Random Insalt Generator

**** PRINT THE LISTS USING A LOOP ****
"""
List1 = ['artless', 'bawdy', 'beslubbering', 'bootless', 'churlish',
'cockered', 'clouted', 'craven', 'currish', 'dankish', 'dissembling',
'droning', 'errant', 'fawning', 'fobbing', 'froward', 'frothy',
'gleeking', 'goatish', 'gorbellied', 'impertinent', 'infectious',
'jarring', 'loggerheaded', 'lumpish', 'mammering', 'mangled',
'mewling', 'paunchy', 'pribbling', 'puking', 'puny', 'qualling',
'rank', 'reeky', 'roguish', 'ruttish', 'saucy', 'spleeny',
'spongy', 'surly', 'tottering', 'unmuzzled', 'vain',
'venomed', 'villainous', 'warped', 'wayward', 'weedy', 'yeasty']


List2  = ['base-court', 'bat-fowling', 'beef-witted', 'beetle-headed',
'boil-brained', 'clapper-clawed', 'clay-brained', 'common-kissing',
'crook-pated', 'dismal-dreaming', 'dizzy-eyed', 'doghearted',
'dread-bolted', 'earth-vexing', 'elf-skinned', 'fat-kidneyed',
'fen-sucked', 'flap-mouthed', 'fly-bitten', 'folly-fallen',
'fool-born', 'full-gorged', 'guts-griping', 'half-faced',
'hasty-witted', 'hedge-born', 'hell-hated', 'idle-headed',
'ill-breeding', 'ill-nurtured', 'knotty-pated', 'milk-livered',
'motley-minded', 'onion-eyed', 'plume-plucked', 'pottle-deep',
'pox-marked', 'reeling-ripe', 'rough-hewn', 'rude-growing',
'rump-fed', 'shard-borne', 'sheep-biting', 'spur-galled',
'swag-bellied', 'tardy-gaited', 'tickle-brained',
'toad-spotted', 'unchin-snouted', 'weather-bitten']


List3 = ['apple-john', 'baggage', 'barnacle', 'bladder', 'boar-pig',
'bugbear', 'bum-bailey', 'canker-blossom', 'clack-dish', 'clotpole',
'coxcomb', 'codpiece', 'death-token', 'dewberry', 'flap-dragon',
'flax-wench', 'flirt-gill', 'foot-licker', 'fustilarian', 'giglet',
'gudgeon', 'haggard', 'harpy', 'hedge-pig', 'horn-beast',
'hugger-mugger', 'joithead', 'lewdster', 'lout', 'maggot-pie',
'malt-worm', 'mammet', 'measle', 'minnow', 'miscreant', 'moldwarp',
'mumble-news', 'nut-hook', 'pigeon-egg', 'pignut', 'puttock',
'pumpion', 'ratsbane', 'scut', 'skainsmate', 'strumpet', 'varlot',
'vassal', 'whey-face', 'wagtail']

newList = []
def insaultGenAuto():
    import random
    global List1, List2, List3
    rn = 0

    for cntr in range(1):
        rn = random.randint(0,50)
        z = str(" {} ".format(List1[rn]))
        for cntr in range(1):
            rn = random.randint(0,50)
            y = str("{} ".format(List2[rn]))
            for cntr in range(1):
                rn = random.randint(0,50)
                x = str("{} ".format(List3[rn]))
            print(("Your random insulat is: ") + str(z) + str(y) + str(x))
        # This is the option to reutn to main menu
            quit = "n"
            
            while(quit == "n"):
                

                quit = input("would you like to quit? y/n ").lower()
                mneu()
            
def insaultGenPick():
    global List1, List2, List3, newList
    
    count = 1
    for col in List1:
        print(str(count) + ": " + "\n" + col)
        count = count + 1
    choice = int(input("Enter the first number: "))
    wordOne = List1[choice-1]
    
    print("\n\n")
    
    count = 1
    for col in List2:
        print(str(count) + ": " + "\n" + col)
        count = count + 1
    choice = int(input("Enter the second number: "))
    wordTwo = List2[choice-1]
    
    print("\n\n")
    
    count = 1
    for col in List3:
        print(str(count) + ": " + "\n" + col)
        count = count + 1
    choice = int(input("Enter the third number: "))
    wordThree = List3[choice-1]

    print(wordOne + " " + wordTwo + " " + wordThree)
            
# This is the option to reutn to main menu
    quit = "n"
    
    while(quit == "n"):
        

        quit = input("would you like to quit? y/n ").lower()
        mneu()
        
def deleteWord():
    global List1, List2, List3
    newList = []
    
    chose = int(input("Deleting items from a list: 1 = List 1, 2 = List 2," +
                  " 3 = List 3: "))
    if(chose == 1):
        for col in List1:
            print(col)
        choice = input("Delete a word from the List: ")
        List1.remove(choice)
        newList = List1
        print(newList)
        # This is the option to reutn to main menu
        quit = "n"
        
        while(quit == "n"):
            

            quit = input("would you like to quit? y/n ").lower()
            mneu()
            
    elif(chose == 2):
        for col in List2:
            print(col)
        choice = input("Delete a word from the List: ")
        List2.remove(choice)
        newList = List2
        print(newList)
        
        quit = "n"
        
        while(quit == "n"):
            

            quit = input("would you like to quit? y/n ").lower()
            mneu()
    elif(chose == 3):
        for col in List3:
            print(col)
        choice = input("Delete a word from the List: ")
        List3.remove(choice)
        newList = List3
        print(newList)

        quit = "n"
        
        while(quit == "n"):
            
    
            quit = input("would you like to quit? y/n ").lower()
            mneu()
     
def addWord():
    global List1, List2, List3
    newList = []
    mnu = """ Adding a word to a List:
            1) List 1
            2) List 2
            3) List 3
        """
    print(mnu)
    chose = int(input("Enter 1 - 3: "))
    if(chose == 1):
        for col in List1:
            print(col)
        choice = input("Add a word to the List: ")
        List1.append(choice)
        newList = List1
        print(newList)
        
    # This is the option to reutn to main menu
        quit = "n"
        
        while(quit == "n"):
            

            quit = input("would you like to quit? y/n ").lower()
            mneu()
    if(chose == 2):
        for col in List2:
            print(col)
        choice = input("Add a word to the List: ")
        List2.append(choice)
        newList = List2
        print(newList)
        
        quit = "n"
        
        while(quit == "n"):
            

            quit = input("would you like to quit? y/n ").lower()
            mneu()
    if(chose == 3):
        for col in List1:
            print(col)
        choice = input("Add a word to the List: ")
        List3.append(choice)
        newList = List3
        print(newList)
        
        quit = "n"
        
        while(quit == "n"):

            quit = input("would you like to quit? y/n ").lower()
            mneu()
        print("\nBye\n")
def addRemoveMenu():
    # Menu for adding and removing
    print("Menu for adding or deleting a word")
    choice = int(input("Please enter 1 or 2:\n 1 = add, 2 = remove: "))
    
    if(choice == 1):
        addWord()
        
    elif(choice == 2):
        deleteWord()
        
    else:
        print("Thats not an Option ")
def mneu():
    menuText = """  Wolcome to Insualt Generator
                    There are 3 modes:
                        1) Randomly be insualted
                        2) Pick an Insualt
                        3) Build an Insault
                """
    print(menuText)
    choice = int(input("Please enter 1 -3 : "))
    
    if(choice == 1):
        insaultGenAuto()
        
    elif(choice == 2):
        insaultGenPick()
        
    elif(choice == 3):
        addRemoveMenu()
        
    else:
        print("Thats not an Option ")
   
def main():
    # quit = "n"
    
    # while(quit == "n"):

    #     quit = input("would you like to quit? y/n ").lower()
        
    
    # print("\nbye")
    # insaultGenAuto()
    # insaultGenPick()
    # deleteWord()
    # addWord()
    mneu()
main()
