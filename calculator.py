import math #Importing math module
import time #Importing time module

def arthmatic(): #creating a function named arithmatic to perform BODMAS operations
    y =input("Enter the BODMAS operation you want to calculate (eg : (3+4-5)*4 ) : ")#asking user to enter a BODMAS operation
    try: #checking wether the equation consists any additional operations
        result = eval(y)
        print(f"The result of the expression {y} is: {result}")
    except Exception as e:
       print(f"\nError: Invalid expression. {e}\n") #letting user know the error
       time.sleep(2.0)
       arthmatic()

def trignomatic(): #creating a tignometric function to perform trignometric operations
    option=["sin","cos","tan","sinh","asin","asinh","acos","acosh","acos","atan","atanh","tanh"] #initilazing a set of trignometric equations
    y = input(f"\nenter the operations you want to perform {option} : ").strip().lower()
    z= float(input("enter the degree : "))
    
    try :
        if y in option: #checking wether the user has coosed with in the given range of options if yes print the result after calculation else printing the mistake
            if y == "tan":
                print(f"{y} ({z}) : {math.tan(math.radians(z))}")#converting entered degree into radian for more accurate answer
            elif y == "sin":
                print(f"{y} ({z}) : {math.sin(math.radians(z))}")
            elif y == "cos":
                print(f"{y} ({z}) : {math.cos(math.radians(z))}")
            elif y == "acos":
                print(f"{y} ({z}) : {math.acos(math.radians(z))}")
            elif y == "acosh":
                print(f"{y} ({z}) : {math.acosh(math.radians(z))}")
            elif y == "cosh":
                print(f"{y} ({z}) : {math.cosh(math.radians(z))}")
            elif y == "asin":
                print(f"{y} ({z}) : {math.asin(math.radians(z))}")
            elif y == "sinh":
                print(f"{y} ({z}) : {math.sinh(math.radians(z))}")
            elif y == "asinh":
                print(f"{y} ({z}) : {math.asinh(math.radians(z))}")
            elif y == "atan":
                print(f"{y} ({z}) : {math.atan(math.radians(z))}")
            elif y == "tanh":
                print(f"{y} ({z}) : {math.tanh(math.radians(z))}")
            elif y == "atanh":
                print(f"{y} ({z}) : {math.atanh(math.radians(z))}")

    except Exception as e:
        print(f"\nError : {e}\n")
        time.sleep(2.0)
        trignomatic()
        

def  log():#creating a log function to perform logalgorithmatic
    x = float(input("\nlog of base : "))#asking user to enter base 
    y= float(input(f"enter the value you want to calculate log "))#asking user to enter value to calculate

    try :
        print(f"log {y} base {x} : {math.log(y,x)}")
    except Exception as e:
        print(e)

def exponential():#creating a exponential function to perform exponential operations
    x = input("\n1.Exponential (e^) \n2.roots(x^y) \nenter : ")#asking user to select from the given options
    try :
        if x == "1":
            y = float(input("\nenter value you want to calculate e^ "))
            print(f"result : {math.exp(y)}")
        elif x == "2":
            y = float(input("\nenter the base : "))
            z= float(input("enter the power (IF YOU WNAT TO CALCULATE SQUARE ROOT ENTER 0. 5) :"))
            print(f"result : {math.pow(y,z)}")
    except Exception as e: 
        print(f"{e} \tchoose from given options") #letting user to know choose from given options
        time.sleep(2.0)
        log()

def intro():
    print("\nwelcom to the calculator ")
    print("selct the operations which u wish to perform : ")
    print("\tOPERATIONS \n1. normal mathematical operations \n2. Trignomatic \n3. Log algorithmatic \n4. Exponential ")#list of operations user can select from
    x=input("Enter the number of the operation you wish to perform : ")
    y=1
    while(y == 1):
        if (x == "1") :
            arthmatic()
            y=0
        elif (x == "2") :
            trignomatic()
            y=0
        elif (x == "3") :
            log()
            y=0
        elif (x == "4") : 
            exponential()
            y=0
        else:
            print("/tPlease choose option from the above given options") 
            intro()
            y=0

if __name__ == "__main__": #if no function is running , run intro()
       intro()
