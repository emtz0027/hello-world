#Section 1
from main_character import money
#Estephania Martinez
#02/03/21

#will print out what the game is about
def start():
    #start of game
    print("Its early morning and Tanjiro decides to help out his mom wake up his siblings.")
    input()
    print("He starts getting ready to head into town to sell charcoal.")
    input()
    print("As he's selling charcoal many people ask him for help.")
    input()
    print("What will Tanjiro do?")
    option = input("A: Help those in need\nB: Keep selling charcoal\n")



#Player will help and as a reward those that were helped will buy charcoal
    if option == 'A':
        print("Tanjiro will help those in need as he encounters them.")
        input()
        print("While helping out many thank him.")
        input()
        print("Due to helping out he ends up selling out of charcoal as well.")
        input()
        print("Each pound of charcoal cost $2 and he sold a total of 30 pounds.")

        
#COME BACK TO AND MAKE FUNCTION RUN
        #print("He ends up with $", money + (60))

        print("He ends up earning $60.")
        

#Playe will continue selling charcoal
    if option == 'B':
        print("Tanjiro decides to continue selling charcoal")
        input()
        print("Someone comes up to him and would like to but charcoal.")
        #print("You tell them 5lbs is $10 and 10lbs is $20")

        #start making calculations
        print("'How much would you like? I sell in bundles of 5lbs and 10lbs', Tanjiro asks.")
        char_pri = 1
        charcoal = 30 #pounds of charcoal you have
        money = 10 #amount of money you have(USD)

#come back and finish
        #player will be selling charcoal in a bundle of 5lbs($10) or 10lbs($20)

        for i in range(char_pri):
           # print("How much would you like? I sell in bundles of 5lbs and 10lbs")
            item = input("A: 5lbs\nB: 10lbs\n").upper()
            if item == 'A':
                    #if char_pri == 0:
                        print("'Here are 5lbs of charcoal it will be $10.' ")
                        print("After a while Tanjiro sells some charcoal and ends up with $40.")
                        
                    #else:
                        print("")
            elif item == 'B':
                print("'Here are 10lbs of charcoal it will be $20.'")
                print("After a while Tanjiro sells some charcoal and ends up with $40.")
                
#engage player more
#Heading back home
    input()
    

            
                
        
    
    
    

#Character heads into town to sell charcoal
#He hears people asking for help

#Player can choose

    #to continue selling charcoal
    #Head back home
    #Help those in need


#Continue selling charcoal
    #makes money to support his family

#head back home
    #player is killed by demons
    #player dies

#help those in need
    #people thank him for his help



start()
