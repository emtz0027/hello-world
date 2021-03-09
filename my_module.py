import random
import math

#my_module
#Estephania Martinez
#04/04/21
#Module 6 Lab Activity


#will print 10 random numbers from a range between 25 and 35
def rand():
    for cube in range(10):
        print(random.randrange(25,35))
#rand()

#will print out a random element from the list
def randomList(x):
    return random.choice(x)
xList = ["a", "apple", 10, 3]

#wil print out an odd integer
def rando():
    return random.randrange(1, 200, 3)

#will print out the answer to the Pythagorean theorem 
def sqrt(a,b):
    c = math.sqrt(math.pow(a,2) + math.pow(b,2))
    return c

