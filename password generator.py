import random #Importing random module
import string #Importing string module
import time #Importing time module

def generate_key(length): #creating a function to generate password of desired length
    syntax = string.ascii_letters(9) + string.digits + string.punctuation #generates password consisting alphabets,digitsang punctuations
    password = ''.join(random.choice(syntax) for i in range(length)) #generating password
    return password

def main():
    try:
        length = int(input("Enter the desired length for your password: "))#asking user to enter desired length of password
        if length < 1: #checking if the user entered length is 1 or not if it is 1 returning error
            print("Password length should be at least 1 character.")
        key = generate_key(length)
        print(f"Your generated password is: {key}")#printing program generated password
    except Exception as e:
        print(f"Invalid input: {e}\n") #printing any exceptions
        time.sleep(2.0)
        main() #running program again after 2 sec duration


if __name__ == "__main__": #if no function is running , run main()
    main()