#define starting variables
directions = []
stop = "go"
inventory = []
current_room = 'Surveillance Room'
valid_commands = ['move', 'yes', 'no', 'q', 'show commands', 'inventory']

move_dictionary = {
        'Surveillance Room' : 0,
        'Rec Room' : 0,
        'Commons' : 0,
        'Terrarium' : 0,
        'Command Room' : 0,
        'Telecommunications Room' : 0,
        'Boarding Room' : 0,
        'Living Quarters': 0
}


intro_dialogue = 'You awaken. Your head is pounding and you cannot remember the last four hours. Second to the \n\
pounding of your head is your urgency to figure out what happened. Who knocked me out and why? \n\
In the distance you hear the humming of the computers as they diligently record every second of the passengers lives. \n\
A "necessary" evil as our commanding officers called it. Or maybe they could have more standards for boarding than a pulse.\n\
It occurs to you that you could review the surveillance logs. Would you like\n\
to review the Surveillance Logs?'

#function for showing instructions
def show_instructions():  
   #print a main menu and the commands
   print("Spaceship Adventure Game")
   print("Collect 6 clues to help discover the saboteur. Or die.")
   print("Move commands: Move")
   print("View inventory: Inventory")
   print("Repeat instructions: instructions")
   print("Quit: q\n")

#function for player movement
def room_description(current_room):
    room_descriptions = {
        'Surveillance Room': '',

        'Rec Room': 'Immediately the sound of exercise machines and hum of recorded \n\
Televised programming from Earth washes over you. For you, as many others, it has a calming effect. \n\
Everyone has a mandatory schedule they must adhere to to be in this room. It occurs to you you could review\n\
the Rec Room Logs. Would you like to review the Rec Room Logs?\n',

        'Commons': 'It\'s lunch-time and everyone is in their respective groups. \n\
Your friend Cassy calls you over to her table. Quickly you relay the urgency of the situation to her. \n\
While at first surprised she nods. She mentions that your crewmates Jody and Rob have been acting suspicious.\n\
After a moment of silence Cassy mentions she saw them exit the terrarium yesterday and thought nothing of it. \n\
Panic crosses her face and she urges you to make sure the life support systems are intact.\n',

        'Terrarium': 'The 10 additional degrees and humidity instantly make your \n\
breath feel heavier. Many agricultural crops in addition to plants genetically engineered to convert \n\
carbon dioxide efficiently are bred in this room. A loud popping sound jolts you from your requiem. \n\
The air pump appears to have been smashed with a wrench. Not good. You notice a scuff on the ground \n\
that looks oddly familiar...Would you like to investigate further?\n',

        'Command Room': 'The captain is nowhere in sight. You take a moment to stare out \n\
at the immeasurable amount of stars and galaxies. The real reason you ever signed up for this mission. \n\
William T Kirk has been Captain of this poor excuse of a ship for years...it\'s odd that he\'s missing. \n\
0800 he\'s always on the deck. Upon asking your crew member they say he\s in the Telecommunications . \n\
While mulling that over you notice a flashing message prompt on the captain\'s terminal.\n\
Would you like to read it? ',

        'Telecommunications Room': 'William has a grave look on his face.  \n\
You overhear the local mercenaries making threats to blow up the ship if a ransom isn\'t paid. \n\
Judging by the look on William\'s face he doesn\'t have that ransom sitting in his shallow pockets. \n\
He gestures to a piece of paper sitting on the table while cradling his head in his hands. \n\
Would you like to read it?\n',

        'Boarding Room': 'It appears that at one point it was barricaded from the inside. \n\
The 4 Saboteurs must\'ve escaped the ship while you were out. An ID Tag is on the floor. \n\
Would you like to pick it up?\n',

        'Living Quarters': 'You\' enter the living quarters. Player, we must stop the story here. For a small fee of $5 \n\
we can continue this story. However, the writer must eat too.\n'
    }

    for rooms in room_descriptions.keys():
        if rooms == current_room:
            print(room_descriptions[rooms])


def player_move(current_room, stop):
#dictionary tracking amount of times room is visited

#room dictionary for navigation
    rooms = {
            'Surveillance Room': {'east': 'Rec Room'},
            'Rec Room': {'east': 'Surveillance Room', 'south': 'Commons'},
            'Commons': {'north': 'Rec Room', 'south': 'Boarding Room', 'west': 'Terrarium', 'east': 'Command Room'},
            'Terrarium': {'west': 'Commons'},
            'Boarding Room': {'north': 'Commons', 'east':'Living Quarters'},
            'Command Room': {'west':'Commons', 'north': 'Telecommunications Room'},
            'Telecommunications Room' : {'south': 'Command Room'},
            'Living Quarters' : {'west': 'Boarding Room'}
        }


#room descriptions to print upon entry into room, once

    while stop == "move":
        print("You are in {} and you can currently move: ".format(current_room,end = ""))
        for direction, room in rooms[current_room].items():
            directions.append(direction)
            print("{} to the {}".format(direction.capitalize(), room))
        # print(directions)
        val = input("Please Enter a Direction").lower()    

        if val == 'q':
            break

        elif val in directions:
            current_room = rooms[current_room][val]
            print("You're now in the {}\n".format(current_room))

            directions.clear()
            stop = 'go'
            break

        else:
            print("Direction is not valid. Try Again.")    

    return current_room

#function for quitting
def player_quit():
    while stop == "quit":
        print("Thanks for playing!!!")


#Function for inventory
def player_inventory():
    print("Your Navi-unit has the following files:")
    for item in inventory:
            print(item)
    # for item in inventory:
    #     print(item)
    #     continue

#Function to grab item
def prompt_yes(current_room, stop):
#dictionary of room items

    room_items = {
        'Surveillance Room' : 'Surveillance Logs',
        'Rec Room' : 'Exercise Schedule',
        'Commons' : '',
        'Terrarium' : 'Growth Logs',
        'Command Room' : 'Mysterious Caller information',
        'Telecommunications Room' : 'Cargo Manifest',
        'Boarding Room' : 'Maintenance Logs'
    }

    item_descriptions = {
        'Surveillance Room' : 'The Surveillance Logs indicate there was an exodus of four passengers after a scuffle. \n\
They rushed to the Boarding room and exited on another ship. While it is obvious they\'re \n\
disguised it may be possible to identify them later. Sighing you save the log to your navi-unit.\n',

        'Rec Room' : 'Reviewing the Rec Room logs you notice something odd. Jody never showed up for her scheduled exercise. \n\
Her , William and Jordan in fact...management cracks down on missing these exercises. They had to have had a reason... \n\
You make a mental note to review the Surveillance logs more closely at a later time and save them to your navi-unit.\n',

        'Commons' : '',

        'Terrarium' : 'The wrench on the ground you recognized easily. Jordan had nearly had your head when you borrowed it \n\
without his permission months back. I suppose stranger family heirlooms have existed. Why would he \n\
sabotage the systems unless he had an escape plan? How long had he had an escape plan. You frantically \n\
review the Growth Logs and realize that growth has been declining for weeks. This plan wasn\'t implemented \n\
on a whim...You save the Growth logs to your navi-unit with a growing sense of doom.\n\
Seems about time to go to the Command Room and get some answers',

        'Command Room' : 'The screen has a rather rude message upon it. There\'s talk of 4 crew who\'ve been undercover \n\
on the ship for what appears to be months. Also mention of gambling debt. Seems they\'re \n\
willing to take that debt out by cashing in the scrap from the remains of our captain\'s ship.\n\
You save the message to your navi-unit. More than likely will need this to explain to your contractor \n\
why you broke your contract so soon. \n\
If you even get off the ship alive at this point....\n',

        'Telecommunications Room' : 'The paper is a cargo manifest from the ship that you could only assume picked up our 4 mutaneers. \n\
Listed are various valuable pieces of cargo we were trucking to Mars. Gonna stash this away on my \n\
navi-unit now...yet another joyful tale for my contractor.\n',


        'Boarding Room' : 'This is the ID tag of your cousin Johnathon. How\'d he get mixed up in all of this? You crease \n\
your brow hoping he\'s alright. Ruefully you stash the ID tag in your jacket pocket. Today \n\
is only getting better and better...\n'

    }

    inventory = room_items[current_room]

    for room in item_descriptions.keys():
        if room == current_room:
            print(item_descriptions[room])
            break

    return inventory 


show_instructions()

print(intro_dialogue)

stop = str(input('So, would you?'))

while stop != "q":
  #  stop = input("Player, what would you like to do?").lower().strip()

    if stop not in valid_commands:
        stop = str(input("Command invalid. Please Try Again or type Show Commands"))

    if stop == 'instructions':
        show_instructions()

    if stop == 'yes':
        inventory.append(prompt_yes(current_room, stop))
        stop = str(input("Player, what next?").lower().strip())

    if stop == 'no':
         stop = str(input("Player, what next?").lower().strip())       

    if stop == 'inventory':
        if len(inventory) == 0:
            print('There are no files. Maybe you should explore')
        else:
            player_inventory()
            
        stop = str(input('Player, what next?'))


    if stop == "q":
        player_quit()

    if stop == "move":
        current_room = player_move(current_room, stop)

        if move_dictionary[current_room] == 0 and current_room != 'Living Quarters':
            room_description(current_room)
            if current_room != 'Commons':
                stop = str(input('Would you like to?'))
            else:
                stop = str(input('Player, what next?'))

        if move_dictionary[current_room] > 1 and current_room != 'Living Quarters':
            if current_room != 'Commons':
                stop = str(input('Would you like to?'))
            else:
                stop = str(input('Player, what next?'))

        move_dictionary[current_room] = move_dictionary[current_room] + 1

        if current_room == 'Living Quarters' and len(inventory) == 6:
            room_description(current_room)
            print("Thanks for playing!")
            stop = 'q'

        if current_room == 'Living Quarters' and len(inventory) < 6:
            room_description(current_room)
            print("It appears you missed a room. You scratch your head in confusion. Something appears to be missing...")
                
     #   while stop != 'yes' and current_room != 'Commons':
     #       stop = str(input('c\'mon player. Play along. Please say yes. Or else.'))
