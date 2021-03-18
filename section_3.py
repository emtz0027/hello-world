#Section 3
#Section 2 head home in the morning option

#Estephania Martinez
#02/03/21

def start():

#morning, finds family dead
    print("It's early morning when Tanjiro is woken up by Mr. Saburo")
    print("Tanjiro thanks him for letting him stay the night")
    input()
    print("As he heads home he slowly starts smelling blood")
    print("Knowing his family is the only one that lives in the mountains he starts imagining the worst.")
    input()
    print("He sees his siblings covered in blood and once he looks inside he sees his\nmom and the rest of his siblings as well.")
    print("He sees someone move. It's Nezuko, his sister, but she looks different.\nShe was turned into a demon. He can only come up with two options.")


#decision to clean
    save = input("A: Kill Nezuko\nB: Take her to a doctor\n")

    if save == 'A':
        print("Tanjiro decides to run and take hold his hatchet.")
        print("'I don't want to see you suffer as a demon, I'm sorry,' Tanjiro says as he swings his hathet towards his sisters neck.")
        input()
        print("He starts to dig six holes, five for his siblings and one for his mom.")
        print("He now lives by himself, full of regret for killing his sister.")
#will end game here
        exit()
    elif save == 'B':
        print("Tanjiro picks up his siter and carries her on his back, heading towards the nearest doctor.")
        print("Nezuko stsrts to move around causing them both to fall over a cliff.")
        input()
        print("'The snow softened my fall,' thinks Tanjiro. 'Where's Nezuko?'")
        print("He spots Nezuko, as he's headed towards her, she attacks him.")
        input()

        print("Tanjiro needs to think quick.")
        safe = input("A: Defend himself\nB: Run and ask for help.")

        if safe == 'A':
                print("Tanjiro gets his hatchet as soon as Nezuko lands on him. She satrts biting the handle.")
                print("'Nezuko it's your brother, Tanjiro!' he screams out.")
                input()
                print("Nezuko starts crying as she rememebers who he is.")
                print("Someone suddenly tries to kill Nezuko but Tanjiro rolls over, protecting her.")
                input()
                print("Giyuu, who tried to kill Nezuko, asks 'You know you're defending a demon, right?")
                print("'She's my sister,' cries out Tanjiro. He continues to explain what happened.")

        if safe == 'B':
                print("Tanjiro runs and comes across Giyuu, a demon slayer, and he explains he wants to save his sister,\nwho turned into a demon.")
                print("Giyuu doesn't like the idea of helping him out as he only has one job, kill demons.")
                input()
                print("After seeing how Tanjiro protects Nezuko and vice versa. He decides to let them go and he sends them off to his teacher")
       
            


#When the next day comes, early in the morning Tanjiro heads home

#When he arrives he discovers his family has been killed
#His sister, Nezuko attacks him, as she is now a demon

#player can choose:
    #Kill Nezuko
    #Try to reason with Nezuko
    #give up

#Kill Nezuko
    #Tanjiro won't be abloe to live with himself afterwards
    #'technically dead in the inside'

#Try to reason with Nezuko
    #Nezuko remembers who Tanjiro is calms down a bit


#might remove this option
#give up
    #player automatically dies
    
#will make program run
start()
