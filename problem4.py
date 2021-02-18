# Estephania Martinez 02/17/21
# Problem 4

# Will use a for loop to go through the number 1 to 50
# if a number is a multiple of 3
# "Divisible by three" will print out
# if a number is a multiple of 5
# "Divisible by five" will print out
# if a number is divisible by both 3 and 5
# "Divisible by both" will prin out
# if its neither
# the number will print out

# listed number between 1 and 50
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
          21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
          31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
          41, 42, 43, 44, 45, 46, 47, 48, 49, 50]:

    # will divide the number above by 3 and 5
    if ((x % 3 == 0) & (x % 5 == 0)):

        #if said number is divisible by both 3 and 5
        #the following will print out next to the number
        print(x, "Divisible by both")

    #will divide the numbers by 3
    elif x % 3 == 0:

        # if said number is divisible 3
        # the following will print out next to the number
        print(x, "Divisible by three")
        
    #will divide the number above by 5
    elif x % 5 == 0:

        #if said number is divisible by 5
        #the following will print out
        print(x, "Divisible by five")

    else:
        print(x)
        
 
