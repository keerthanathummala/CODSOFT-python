import random #importing the random function for the computer's choice
def rules(): 
    print("\nRULES")
    print("\tRock beats Scissors \n\tScissor beats Paper \n\tPaper beats Rock") #displaying the rules of the game

def user_choice():
    user=input("pick from Rock or Paper or Scissors : ").lower() #asking user to choose from the option "rock","paper","scissors"
    while user not in ("rock","paper","scissors"):
        print("please choose from the options : Rock , Paper ,Scissors\n")
        user=input("what would you like to pick Rock or Paper or Scissors : ").lower()
    return user #returning user choice

def comp_choice():
    options=["rock","paper","scissor"]
    return random.choice(options) #returning computers choice

def results():
    user=user_choice() #calling user _choice
    comp=comp_choice() #calling comp_choice() 
    if user == comp:
        print("tie")
    elif (user == 'rock' and comp == 'scissors') or \
         (user == 'paper' and comp == 'rock') or \
         (user == 'scissors' and comp == 'paper'):
        print(f"\nuser coice : {user} \ncomputer choice : {comp}") #printing user and computer choices
        print("You win!")
        z= input("\tplay again yes/no : ").lower() #asking if the user wants to play the game
        if (z == "yes") or (z == "y"):
                results()
        elif (z == "no") or (z == "no"):
                intro()
    else:
        print(f"user coice : {user} \ncomputer choice : {comp}")
        print("You lose!")
        z= input("\tplay again yes/no : ").lower() #asking if the user wants to play the game
        if (z == "yes") or (z == "y"):
                results()
        elif (z == "no") or (z == "no"):
                intro()
    
def intro():    
    print("\nWelcome to the game Rock Paper Scissors")
    y=1
    while(y == 1): #creating a while loop just incase user doesn't want to choose from the options
        x=input("please select \n1. Rules \n2. Start the game \n").lower()
        if (x =="rules") or (x == "1"):
            y=0
            rules() #displaying the rules
            z= input("\t\tback yes/no : ").lower() #asking if the user wants to return to homepage or not
            if (z == "yes") or (z == "y"):
                intro()
            elif (z == "no") or (z == "no"):
                pass

        elif (x == "start the game") or (x == "2"):
            y=0
            print(results())

            z= input("\tplay again yes/no : ").lower() #asking if the user wants to play again or not
            if (z == "yes") or (z == "y"):
                results()
            elif (z == "no") or (z == "no"):
                intro()
            
        else :
            print("please select from the above option : ")
            y = 1
if __name__ == "__main__":
    intro()



