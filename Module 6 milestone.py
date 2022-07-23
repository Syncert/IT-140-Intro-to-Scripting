#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.


#Sample function showing the goal of the game and move commands
def show_instructions():  
   #print a main menu and the commands
   print("Dragon Text Adventure Game")
   print("Collect 6 items to win the game, or be eaten by the dragon.")
   print("Move commands: Move")
   print("Add to Inventory: grab item")
   print("Quit: q\n")

#In this solution, the player’s status would be shown in a separate function.
#You may organize your functions differently.

valid_commands = ['move', 'grab item', 'q', 'show commands']

rooms = {
        'Great Hall': {'south': 'Bedroom'},
        'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
        'Cellar': {'west': 'Bedroom'}
    }


current_room = 'Bedroom'
directions = []
stop = "go"
found = False
show_instructions()


while stop != "q":
    stop = input("Player, what would you like to do?").lower()
    if stop not in valid_commands:
        print("Command invalid. Please Try Again or type Show Commands")

    if stop == 'show commands':
        show_instructions()


    if stop == "q":
        print("Thanks for playing!")
        break

    while stop == "move":
        print("You are in {} and you can currently move: ".format(current_room,end = ""))
        for direction, room in rooms[current_room].items():
            directions.append(direction)
            print("{} to the {}".format(direction.capitalize(), room))

        print(directions)
        val = input("Please Enter a Direction").lower()    

        if val == 'q':
            break

        elif val in directions:
            current_room = rooms[current_room][val]
            print("You're now in the {}".format(current_room))
            directions.clear()
            break

        else:
            print("Direction is not valid. Try Again.")        


