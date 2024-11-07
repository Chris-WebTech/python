# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:21:10 2023

@author: christophernmiller

"""
print("Welcome to 2023 Calculator 2.0!")
print("\n")


# Greetings function - get input from user
def Greetings():
    
    #inputs
    fName = input("Enter first name here: ")
    lName = input("Enter last name: ")
    cFrom = input("Enter the City that you are From: ")
    
    # Display First Name Last Name with greetings
    print("Greetings " + fName + "   " + lName + " From " + cFrom + "   ")

# Recieve computer input - calculate response
def areaOfTriangle_b(ht, wd):
    
    # variables
    answer = 0.0

    # calculations
    answer = 1.0/2.0 * ht * wd

    # print ans
    print("area of Triangle B is : " + str(answer))

# Recieve user iput calculate response
def areaOfTriangle_c(ht,wd):
    
    # Veriables
    ans = 0.0

    # user now gives inputs
    ht = float(input("Enter the Hieght: "))
    wd = float(input("Enter the Width: "))

    # calculate answer as ans
    ans = 1.0 / 2.0 * ht * wd
   
    # Display Answer
    print("Area of Triangle C is: " + str(ans))

    return ans
    
# Ask the user for a speed in mph and convert it knots.
def mPHToKnots():
    
    print("Convert MPH to KNOTs - ")
    
    # Integers
    MH = float(input("Your speed in MPH: "))
    K = 1.151

    # Calculate
    SP = ( MH / K )
    SP = round(SP, 2)

    # Display the answer.
    print("Your Speed in Knots: " + str(SP))
    print("\n")
    
    
# Ask the user for a speed in knots and convert it mph. 
def kNotsToMPH():
    
    print("Calculate Knots to MPH")

    #integers
    K2 = 0
    MP = 0

     #calculate
    SP2 = ( MP * K2 )
    SP2 = round(SP2, 2)

    # Display the answer.
    print("Your Speed in MPH: " + str(SP2))
    print("\n")


# Ask the user for three numbers, average the numbers.
def mean1():
    print("Give three different numbers for there avverage")

    #integers
    N1 = float(input("First Number: "))
    N2 = float(input("Second Number: "))
    N3 = float(input("Third Number: "))
    N4 = 3.0

    #calculate
    aNsw = ( N1 + N2 + N3 / N4)
    aNsw = round(aNsw, 2)

    # display the answer
    print("The Average is:" + str(aNsw))
    print("\n")
    
# Ask the user for the monthly salary and the number of months they have worked at that salary.
def gross():
    
    print("Colaculate your gross pay - ")
    salary = float(input("Your current monthly pay: "))
    months = float(input("How many Months you have worked"))
    
    # Calculate the gross pay for that time period.
    ans = salary * months

    # display the answer.
    print("Your current gross pay is: " + str(ans))
    
# Ask the user for a Fahrenheit temperature and convert it to Celsius. 
def frht():
    print("\nConvert Ferenheit to Celcius.")
    
    F = float(input("Temperature in Ferenheit: "))

    #integers
    A = 5.0
    B = 9.0
    D = 32.0

    #calculate
    celcius = (F - D) * A / B
    celcius = round(celcius, 2)

    # Display the answer
    print("Temprature in Celcius " + str(celcius))
    print("\n")


# Five Celcius and convert to Fehrenheit
def celciuse():
    print("Calculate temperature from Celcius to Ferhenheit")

    #integers
    C2 = float(input("Temperature in Celcius: "))
    A2 = 9.0
    B2 = 5.0
    D2 = 32

    #calculate
    frhn = (A2 / B2 * C2 + D2)
    frhn = round(frhn, 2)

    # Display answer
    print("Temprature in Farhenheit: " + str(frhn))
    print("\n")

# run program    
def main():
    
#------------------  Run Greetings  ---------------
    Greetings()
#------------------ Run Traiangles  ---------------
    ht = 4.0
    wd = 10.0
    
    areaOfTriangle_b(ht,wd)
    print("\n")
    
    # Q2c
    areaOfTriangle_c(ht,wd)
    print("\n")
    
#------------------ Calculate Speed  ---------------

    mPHToKnots()
    
#------------------ Calculate Speed   ---------------

    kNotsToMPH()
    
#------------------ Calculate 3 Number Mean  --------
    mean1()
    
#------------------ Calculate 3 Number Mean  --------
    gross()
    
#------------------  Fahrenheit to Celsius  ---------
    frht()
    
#------------------ Celsius to Fahrenheit  ----------
    celciuse()

main()
