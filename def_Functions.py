# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:21:10 2023

@author: christophernmiller

"""
# 1 Write a function that asks the user their first name, last name and the city where they live.
#Display the greeting that welcomes them with their first and last name and it includes the city from
#where they live – i.e. Hello Bubba Jones from Kalispell.
print("Welcome to Wake Yake Calculator 2.0!")
print("\n")

def Greetings():
    
    #inputs
    fName = input("Enter first name here: ")
    lName = input("Enter last name: ")
    cFrom = input("Enter the City that you are From: ")
    
    # Display First Name Last Name with greetings
    print("Greetings " + fName + "   " + lName + " From " + cFrom + "   ")

    
# 2a. Where the main program provides the base and height and the function returns
#the answer (like add2nums_a)

def areaOfTriangle_a(ht,wd):
    
    # Veriables
    ans = 0.0
    
    #Calculations
    ans = 1.0/2.0 * ht * wd
    
    #Return Function
    return ans
# Q2_b
def areaOfTriangle_b(ht, wd):
    
    # variables
    answer = 0.0

    # calculations
    answer = 1.0/2.0 * ht * wd

    # print ans
    print("area of triangle B is : " + str(answer))
    
    
# Q2_c
def areaOfTriangle_c(ht,wd):
    
    # Veriables

    ans = 0.0
    ht = float(input("Enter the Hieght: "))
    wd = float(input("Enter the Width: "))
    # calculate
    ans = 1.0 / 2.0 * ht * wd
   
    print("Area of Triangle C is: " + str(ans))
    # Display Answer
    return ans

# Q2_d 
def areaOfTriangle_d():
    
    # variable
    ht = 0.0
    wd = 0.0
    ans = 0.0

    # ask for input
    ht = float(input("Enter width: "))
    wd = float(input("Enter Height: "))

    # calculator
    ans = 1.0 / 2.0 * ht * wd
    
    print("Area of triangle D: " + str(ans))

    # return the answer
    return ans
    
# Q3 Ask the user for a speed in mph and convert it knots. Display the answer.
def mPHToKnots():
    
    print("Convert MPH to KNOTs - ")
    
    #integers
    MH = float(input("Your speed in MPH: "))
    K = 1.151

     #calculate
    SP = ( MH / K )
    SP = round(SP, 2)

    print("Your Speed in Knots: " + str(SP))
    print("\n")
    
    
# Q4 Ask the user for a speed in knots and convert it mph. Display the answer.
def kNotsToMPH():
    
    print("Calculate Knots to MPH")

    #integers
    K2 = 0
    MP = 0

     #calculate
    SP2 = ( MP * K2 )
    SP2 = round(SP2, 2)

    print("Your Speed in MPH: " + str(SP2))
    print("\n")


# Q5 Ask the user for three numbers, average the numbers and display the answer
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

    print("The Average is:" + str(aNsw))
    print("\n")
    
# Q6 Ask the user for the monthly salary and the number of months they have worked at that salary.
#Calculate the gross pay for that time period and display the answer.
def gross():
    
    print("Colaculate your gross pay - ")
    
    salary = float(input("Your current monthly pay: "))
    months = float(input("How many Months you have worked"))
    

    ans = salary * months
    print("Your current gross pay is: " + str(ans))
    
# Q7 Ask the user for a Fahrenheit temperature and convert it to Celsius. Display the answer
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

    
    print("Temprature in Celcius " + str(celcius))
    print("\n")


# Q8 Five Celcius and convert to Fehrenheit
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

    print("Temprature in Farhenheit: " + str(frhn))
    print("\n")

    
def main():
    

#------------------Question 1---------------
    Greetings()
#------------------Question 2a-d------------
    # Q2a
    # Veriables the main() program will previde
    ht = 4.0
    wd = 5.0
    
    ans = areaOfTriangle_a(ht,wd)    
    print("Area of triangle A is: " + str(ans))
    print("\n")
    
    # Q2b
    ht = 4.0
    wd = 10.0
    
    areaOfTriangle_b(ht,wd)
    print("\n")
    
    # Q2c
    areaOfTriangle_c(ht,wd)
    print("\n")
    
    # Q2d
    areaOfTriangle_d()
    print("\n")
    
#-----------------Question 3-----------------
    mPHToKnots()
    
#-----------------Question 4-----------------
    kNotsToMPH()
    
#-----------------Question 5-----------------
    mean1()
    
#-----------------Question 6-----------------
    gross()
    
#-----------------Question 7-----------------
    frht()
    
#-----------------Question 8-----------------
    celciuse()

main()
