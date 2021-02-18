#Estephania Martinez 02/17/21
#Problem 3

#Will take input from user, 10 numbers, and print out their average

#x = int(input("Input 10 numbers"))
#for x in input
 #   x *3

x, y, z, avg = 0, 0, 0, 0

#asking user for 10 numbers
print("Enter 10 numbers to find their average")

#will take in input and turn them into integers
x = int(input())

#for loop starts
for z in range (9):

    #takes in input and turns them into intergers as well
    y = int(input())
    avg += y

avg /= 10
#will print out average
print(avg)



