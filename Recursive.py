# -*- coding: utf-8 -*-
"""
Christopher Miller
09/19/2023
Assingment
"""
def BOB(numBottles):
    
    if(numBottles > 0):
        temp = numBottles - 1
        print(str(numBottles) + " bottles of beer on the wall " +
              str(numBottles) + " bottles of beer")
    
        print(" Take one down pass it around " + 
              str(temp) + " bottles of beer on the Wall")
    
        BOB(numBottles - 1)
    
    
def main():
    BOB(100)
main()
