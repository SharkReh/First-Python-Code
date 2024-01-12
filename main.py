# for loading screen code
import time
# the info questions
name = input("What is your name? ")
print("You Name is " + name)
lastName = input("What is your lastname? ")
print("You lastname is " + lastName)
# For only using numbers in age verification
def age_verification():
    try:
      age = int(input("what is your age? "))
      print("You are ", age, " years old.")
    # Code for verification if you are 18
      if age >= 18:
          print("You are verified now!")
      else:
          print("You are unfortunatly a minor")
    except ValueError: 
        print("Please use only numbers for age!")
age_verification()
#For checking if its true or not
print("Are these informations right?")
def right_button():
    reply = input("Are you sure? (Yes/No): ")
    #code for what comes next
    if reply == 'Yes':
        print("Accepted!")
        array1 = [name, lastName, age]
        print(array1)
        print("What can i do for you?")
        print("1.")
        print("2.")
        print("3.")
        numberChoice = input("Enter the number of your desired task.")
        if numberChoice == "1":
            firstTask()
        elif numberChoice == "2":
            secondTask()
        elif numberChoice == "3":
            thirdTask()
            
        else:
            print("Please write a Number of 1,2 or 3!")
    else:
        print("Not Accepted, try again")
# The first Task
import random 
def firstTask():
    print("You have chosen first Task!")
    print("Welcome to Rock, Paper, Scissors!")
    ropasctutorial = input("Do you need a little tutorial?  (Yes/No):")
    if ropasctutorial == "Yes":
         print("The rules are simple: choose one of the three objects (scissors, rock or paper) to beat the computer. \nScissors win against paper \nPaper wins against rock \nRock wins against scissors")
         ropasc()
    else:
        print("Then the game can begin!")
        ropasc()
# For Rock, Paper and Scissors
def ropasc():
    print("Choose one of the objects 1. Scissors 2. Rock 3. Paper")
    gameChoice = input("Enter the number of your choice: 1. 2. or 3. : ")
    if gameChoice in ["1", "2", "3"]:
        theChoices = ["Rock", "Paper", "Scissors"]
        user_choice = theChoices[int(gameChoice) -1]
        computerChoices = random.choice(theChoices)
        print("Your choice is: " + user_choice) 
        print("The computer choice is: " + computerChoices)
        scissors = "Scissors"
        rock = "Rock"
        paper = "Paper"
        if (computerChoices == rock and user_choice == paper) or \
            (computerChoices == scissors and user_choice == rock) or \
            (computerChoices == paper and user_choice == scissors):
            print("You win!")
        elif computerChoices == user_choice:
           print("It's a tie!")
        else:
            print("Computer wins!") 

    else: 
        print("please write a right number")
# For secong task
def secondTask():
    print("You have chosen second Task!")
    print("This is a calculator")
    calculator()
def calculator():
    firstNumber = input("What is your first number?: ")
    secondNumber = input("What is your second number?: ")
    operator = input("What is the operator?: ")
    outcome = 0
    if operator == "+":
        outcome = int(firstNumber) + int(secondNumber)
    elif operator == "-":
        outcome = int(firstNumber) - int(secondNumber)
    elif operator == "*" or operator == "x":
        outcome = int(firstNumber) * int(secondNumber)
    elif operator == "/" or operator == ":":
        outcome = int(firstNumber) / int(secondNumber)
    else: 
        print("False number or operator, please try again")
    print("Result: ", outcome)
# For third task

def thirdTask():
    print("You have chosen third Task!")
    print("It is head or tails!")
    flip_coin = input("You want to flip the coin? (Yes/Not): ")
    if flip_coin == "Yes" and "yes":
        print("The coin is flipped! ")
        head_or_tails = ("head!", "tail!")
        from random import sample 
        print("The coin shows", sample(head_or_tails, k=1))
    else:
        print("please wait! ")
right_button()


    

#def loading():
#            print("Trying to load... ", end="", flush=True)
#            for _ in range(5):
#                  time.sleep(1)
#            print("\nLoading complete!")
#loading()