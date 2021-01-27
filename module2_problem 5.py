#Store wants a self checkout  machine.
#each item has its own price


print()

print("Problem 5:")
#Problem 5

def store():
    #greets customer
    print ("Good morning/afternoon")
    
    #aks for amount of sodas being bought then turns input into an integer
    sodas = int(input("How many sodas are you purchasing?"))
    
    #aks for amount of pocky being bought then turns input into an integer
    pocky = int(input("How many boxes of Pocky are you purchasing?"))
    
    #aks for amount of flowers being bought then turns input into an integer
    flower = int(input("How many flowers are you purchasing?"))
    
    #aks for amount of crackers being bought then turns input into an integer
    crackers = int(input("How many crackers are you purchasing?"))
    
    #takes the customers input and multiplies it by its corresponind price
    Total = (((sodas * 1.57) + (pocky * 1.09) + (flower * 2.99) +
            (crackers * 1.50)))
    
  #  lets customer know their total
    print ("Your total is: $", Total)

    #prints out a goodbye
    print ("Thanks for visiting, please come again.")

    return Total
store()



