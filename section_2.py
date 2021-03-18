#Section 2
#Estephania Martinez
#02/03/21

#After helping those in need Tanjiro decides to head home
#late at night
#A family friend invites him to stay the night,
#as he warn demons lurk the most at night

#Player can choose
    #stay the night
    #continue his jounrye home

#Stay the night
    #player survives another day

#Continue his journey home
    #Encounters a demon and is killed

def start():

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
            print("'I should've stayed' Tanjiro thinks as he feel chills coming up his spine. As he approaches his house he starts smelling blood")
            print("Upon seeing his house he sees his siblings covered in blood")
            input()
            print("'Did I miss one?' says a strange voice")
            print("Tanjiro feels chills as he slowly turns around and sees a demon headed his way.")
            input()

            
#defend himself
            print("'What do I do?' though Tanjiro")
            defense = input("A: Fight with his hatchet\nB: Run away\n")
            if defense == 'A':
                    print("Tanjiro decides to fght the demon and avenge his family.")
                    input()
                    print("The demon ran up to him, trying to cut his head off, but Tanjiro kept dodging his swings.")
                    print("The demon became frustrated that Tanjiro wouldn't go down as easy as his family.")
                    input()
                    print("Tanjiro took notice of how the demon was getting distracted with his own thoughts.")
                    print("He proceded to swing at the demons neck, successfully killing him.")

#run away                    
            if defense == 'B':
                print("Before taking a step to run away, the demon caught up to him.")
                print("Tanjiro regretted not staying at Mr. Saburos house.")
                input("'I hope they didn't suffer,' was Tanjiros last thought as he slowly drifted away.")

                #will quit game here
                exit()

                    

                
           
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

