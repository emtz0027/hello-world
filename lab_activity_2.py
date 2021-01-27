#Follow the instructions on the Lab Activity 2 sheet.
#This file should run without error and print the correct outputs


#Problem 1:
def say_hello():
    name = input("What is your name?")
    print("Nice to meet you " + name + ".")
    #Ask for the user's name
    #print their name with a nice message


#Problem 2:
def bmi():
    height = int(input("What is your height in inches?"))
    weight = int(input("What is you weight in pounds?"))
    return (weight / (height*height)) * 703
print (bmi)    
    #Ask for a user's height and weight
    #Be sure to put both into variables
    #Type out the equation on the assignment sheet
    #return the result of the equation
    

#Problem 3:
def total(price, amount):
    #price = int(input("Price: "))
    #amount = int(input("Amount: "))
    return (price * amount)
    
    #Multiply the price of an item by the amount purchased
    #Return the total owed
    
    
#Problem 4:
def add_up(num1, num2, num3):
    return (num1 + num2 + num3)
    #add the three parameters together and return the result





#***************************************
#Testing code
#
#DO NOT CHANGE ANY CODE BELOW THIS LINE
#***************************************

print("Problem 1:")
#Problem 1
#This should print the user's name along with a nice message.
say_hello()

print()

print("Problem 2:")
#Problem 2
#This line should display a user's bmi based on their height and weight
bmi = round(bmi(),2)
print("Your bmi is: ", bmi)

print()

print("Problem 3:")
#Problem 3
#This should print 67.2
print("Your  total is: ", round(total(5.60, 12),2))
#This should print 59.96
print("Your other total is: ", total(14.99, 4))

print()

print("Problem 4:")
#Problem 4
#This should print 27
print("First add_up test: ", add_up(6, 9, 12))
#This should print 152
print("Second add_up test: ", add_up(45, 8, 99))








