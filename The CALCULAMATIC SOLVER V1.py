#  NEW AND IMPROVED CALCULAMATIC                            Phython Programming
#  Jaeden Olson   10/22/24

#  Create a Python program that simulates a basic calculator.

print('Welcome to the "CALCULAMATIC SOLVER V1"')
print('This program allows you to input an equation of your choosing (2 Variables Only)')
print("")

further = True
while further == True:
    #Asks User to input key stuff
    num1 = float(input("To start the program, please input a value: "))
    num2 = float(input("Please input another value: "))
    oppr = input("Finally, please input an appropriate operator (+,-,*,/): ")
    print("")

    #Checks if opperator is a valid input
    if oppr == "+" or oppr == "-" or oppr == "*" or oppr == "/":
        print("VALID INPUT - COMMENCING CALCULATION. . .")

        #Adds
        if oppr == "+":
            total = format(num1+num2,'.2f')
            print("Your two value",num1,"and",num2,"both add up to be:",total)
            print("")

            #Asks User if they want to continue
            keep = input("Would you like to make more calculations? ")
            #Restarts Program
            if keep == "Yes" or keep == "yes" or keep == "y" or keep == "Y":
                print("Understood - RESETTING PROGRAM. . .")
                print("")                
                pass
            #Both Stop Program
            elif keep == "No" or keep == "no" or keep == "n" or keep == "N":
                print("Understood - SHUTTING DOWN PROGRAM. . .")
                further = False
            else:
                print("ERROR - INVALID STATEMENT - SHUTTING DOWN PROGRAM")
                further = False
                    
        #Subtracts
        if oppr == "-":
            total = format(num1-num2,'.2f')
            print("Your two value",num1,"and",num2,"both add up to be:",total)
            print("")
            
            #Asks User if they want to continue
            keep = input("Would you like to make more calculations? ")            
            #Restarts Program
            if keep == "Yes" or keep == "yes" or keep == "y" or keep == "Y":
                print("Understood - RESETTING PROGRAM. . .")
                print("")
                pass
            #Both Stop Program
            elif keep == "No" or keep == "no" or keep == "n" or keep == "N":
                print("Understood - SHUTTING DOWN PROGRAM. . .")            
                further = False
            else:
                print("ERROR - INVALID STATEMENT : SHUTTING DOWN PROGRAM")
                further = False
                    
        #Multiplies
        if oppr == "*":
            total = format(num1*num2,'.2f')
            print("Your two value",num1,"and",num2,"both add up to be:",total)
            print("")
            
            #Asks User if they want to continue
            keep = input("Would you like to make more calculations? ")
            #Restarts Program
            if keep == "Yes" or keep == "yes" or keep == "y" or keep == "Y":
                print("Understood - RESETTING PROGRAM. . .")
                print("")
                pass
            #Both Stop Program
            elif keep == "No" or keep == "no" or keep == "n" or keep == "N":
                print("Understood - SHUTTING DOWN PROGRAM. . .")
                further = False                
            else:
                print("ERROR - INVALID STATEMENT : SHUTTING DOWN PROGRAM")
                further = False

        #Checks if either vals equal 0
        #Safely shuts down program to protect the CALCULAMATIC SOLVER                
        if oppr == "/" and num1 == 0 or num2 == 0:
            print('ERROR - VALUE(S) DEFINED AS "0" - EMERGENCY SHUTDOWN!')
            further = False
            pass
        #Divides
        elif oppr == "/":
            total = format(num1/num2,'.2f')
            print("Your two value",num1,"and",num2,"both add up to be:",total)
            print("")
            
            #Asks User if they want to continue
            keep = input("Would you like to make more calculations? ")            
            #Restarts Program
            if keep == "Yes" or keep == "yes" or keep == "y" or keep == "Y":
                print("Understood - RESETTING PROGRAM. . .")
                print("")
                pass
            #Both Stop Program
            elif keep == "No" or keep == "no" or keep == "n" or keep == "N":
                print("Understood - SHUTTING DOWN PROGRAM. . .")
                further = False
            else:
                print("ERROR - INVALID STATEMENT : SHUTTING DOWN PROGRAM")
                further = False
                    
    #Returns Error Message
    else:
        print("ERROR - INVALID OPPERATOR, TRY AGAIN")
        print("")


