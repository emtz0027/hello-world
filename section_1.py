#Section 1

#Estephania Martinez
#02/03/21

#will print out what the game is about
def start():
    #start of game
    print("Its early morning and Tanjiro decides to help out his mom wake up his siblings")
    input()
    print("He start getting ready to head into town to sell charcoal")
    input()
    print("As he's selling charcoal many people ask him for help")
    input()
    print("Would will Tanjiro do?")
    option = input("A: Help those in need\nB: Keep selling charcoal\n")



#Player will help and as a reward those that were helped will buy charcoal
    if option == 'A':
        print("Tanjiro will help those in need as he encounter them")
        input()
        print("While helping out many thank him")
        input()
        print("Due to helping out he ends up selling out of charcoal as well")
        input()
        print("Each pound of charcoal cost $2 and he sold a total of 30 pounds")
        print("He ends up with $60 and decides to go back home")

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
                        print("Here are 5lbs of charcoal it will be $10.")
                        print("After a while Tanjiro sells some charcoal and ends up with $40")
                        
                    #else:
                        print("")
            elif item == 'B':
                print("Here are 10lbs of charcoal it will be $20.")
                print("After a while Tanjiro sells some charcoal and ends up with $40")
                
#engage player more
#Heading back home
    input()
    print("As it was getting dark, Tanjiro heads back home")
    input()
    print("As he was walking through a pathway he came across Mr. Saburo")
    input()
    print("Upon seeing Tanjiro through his window he decides to head outside")
    input()
    print("'Hello, Tanjiro, are you heading back home?'\n")
    print("'Yes, I am' replied Tanjiro.")
    print("'You should stay the night. There may be demons roaming around'\n")
    print("What will Tanjiro do?")
    home = input("A: Stay the night in Mr. Saburo's House\nB: Head back home\n")

    if home == 'A':
        print("Tanjiro decides to stay the night as it will be safer")
        input()
        print("'Have you eaten yet?' Mr. Saburo asks.")
        conv = input("A: Yes, I have thank you\nB: No, I haven't\n")

        if conv == 'A':
                print("Alright, well you can put your things aside and sleep here.")
        if conv == 'B':
            print("'I'll make something quick, would you like ramen or something else?'")
            food = input("A: Ramen\nB: Something else")
            if food == 'A':
                print("Sounds good, I'll call you when it's ready")
                print("After eating both Tanjiro and Mr. Saburo go to sleep")
            if food == 'B' :
                print("Ok, I'll make something quick, make yourself at home")
                print("Mr. Saburo ended up making simple rice. After eating they went to bed")
    if home == 'B':
            print("'Stay safe then and make sure to not stray from the pathway,' Mr. Saburo warns him.")
            input()
            print("'I should've stayed' Tanjiro thinks. As he approaches his house he starts smelling blood")
            print("Upon seeing his house he sees his sibling covered in blood")
            print("'Did I miss one?' says a strange voice")
            print("Tanjiro feels chills as he slowly turns around and sees a demon headed his way")
            print("Before he could react the demon had killed him along with his family.")
#might add a short fighting scene afterwards

            
                
        
    
    
    

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
