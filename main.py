import random

computerchoice = random.randint(0,101)

user_input = int(input("Guess a number."))
while user_input != computerchoice:
     if user_input > computerchoice :
       print("your number is too high")
       user_input=int(input("Enter a number"))
     elif user_input< computerchoice:
         print("Your number is too low")
         user_input=int(input("Enter a number"))
print ("Guessed it right")