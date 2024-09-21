#Joy and Beauty of Data
#Assingment1.0
#Christopher Miller
#09/01/23


#Q1 - Enter Your name
print("Entire Your Name")

FN = input("First Name: ")
LN = input("Last Name: ")

print("\n")
print( "Hello " + FN + " " + LN)
print("\n")
print("Welcome To Yake Wake Calculator")
print("\n")

 #-------------------
 
#Q2 - Give Fahrenheit temperature and convert it to Celsius
print("Calculate Temprature from Farhenheit to Celcius")

F = float(input("Temperature in Ferenheit: "))

#integers
A = float(5.0)
B = float(9.0)
D = float(32.0)

#calculate
celcius = (F - D) * A / B
celcius = round(celcius, 2)

print("Temprature in Celcius " + str(celcius))
print("\n")


#Q3 Five Celcius and convert to Fehrenheit
print("Calculate temperature from Celcius to Ferhenheit")

#integers
C2 = float(input("Temperature in Celcius: "))
A2 = float(9.0)
B2 = float(5.0)
D2 = float(32)

#calculate
frhn = (A2 / B2 * C2 + D2)
frhn = round(frhn, 2)

print("Temprature in Farhenheit: " + str(frhn))
print("\n")

#--------------------------------

#Q4 Ask the user for a speed in mph and convert it knots
print("Calculate MPH to Knots")

#integers
MH = float(input("Your speed in MPH: "))
K = float(1.151)

 #calculate
SP = ( MH / K )
SP = round(SP, 2)

print("Your Speed in Knots: " + str(SP))
print("\n")

#------------------------------------

#Q5 Ask the user for a speed in knots and convert it mph


print("Calculate Knots to MPH")

#integers
K2 = float(input("Your speed in Knots: "))
MP = float(1.151)

 #calculate
SP2 = ( MP * K2 )
SP2 = round(SP2, 2)

print("Your Speed in MPH: " + str(SP2))
print("\n")

#--------------------------------------

#Q6 Ask the user for three numbers, average the numbers

print("Give three different numbers for the avverage")

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

#------------------------------------------

#Q7  Ask the user for length, width, and thickness and calculate board feet in inches
print("Calculate Board Feet in Inches")

#integers
M1 = float(input("Width (in inches): "))
M2 = float(input("Length (in inches): "))
M3 = float(input("Thickness (in inches): "))
m4 = 144.0


#calculate

BF = ( M1 * M2 * M3 / m4)
BF = round(BF, 2)

print("The board feet (in inches) is: " + str(BF))

print("\n")
      
print("Thanks For using the Wake Yake Calculatior!")
