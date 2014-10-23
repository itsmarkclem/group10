#!/usr/bin/python3

from FGmap import rooms
from FGplayer import *
from fgitems import *
from FGgameparser import *
import sys



def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    result = ""
    for key in items:
        result += key["name"] + (", " if not key == items[len(items) - 1] else "")
    return result



def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Robs"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    items = room["items"]
    x = list_of_items(items)
    if items != []:
        print("There is " + x + " here." + "\n")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    x = list_of_items(items)
    if items != []:
        print("You have " + x + "." + "\n")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Robs"])
    <BLANKLINE>
    ROBS' ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Rob Evans and Rob Davies. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    # Display items in room
    print_room_items(room)
    #
    # COMPLETE ME!
    #

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "Robs' room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "Robs' room")
    GO SOUTH to Robs' room.
    """

    if rooms[current_room["exits"][direction]]["isvisible"]==True:
        print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to Robs' room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:" + "\n")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")

    for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop your " + item["id"] + ".")

    #
    # COMPLETE ME!
    #
    
    print("\n" + "What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits

def interrogation_place():
    isvalid = False
    while isvalid == False:
        print("1. Where were you last night?")
        print("2. Why did you kill Sarah last night?")
        print("3. There is no need for words. Punch him in the face.")
        print("4. Don't ask him anything.")

        choice= str(input("What do you choose? Type the number,"+"\n"+"> "))
        if choice =="1" or choice =="2" or choice =="3" or choice =="4":
            isvalid = True
        else:
            print("\n"+"That is not a valid input."+"\n")

    if choice == "1":
        print("""I was at the bar with Sarah. Why?
'She's been found dead. We were wondering if you had anything to do with it.
Jack knocks the door and enters the room.
Jack: 'Durden, it's okay, we're wasting this man's time...""")
        print("Conveniently, Claire is the suspect's girlfriend and clears him for last night- he was home before the time of the murder.")
        item_alibi["karma"] = 5   
    elif choice == "2":
        print("""Fuck off, Sarah's dead? I honestly didn't know. I wasn't there.
'That's awfully convenient for you, isn't it, Stuart... We know you were there. We have proof.'
Jack bursts into the room.
Jack: 'He may be lying on that part, but he's an innocent man, Durden. You're free to go, Stuart, but try and be a bit more honest next time, will you.'""")
        print("Conveniently, Claire is the suspect's girlfriend and clears him for last night- he was home before the time of the murder.")
        item_alibi["karma"] = -5   
    elif choice == "3":
        print("""You get dragged out of the room and your partner yells at you.
Jack: 'Get the fuck out of here, Durden. What the hell was that?! Just leave, Durden.'""")
        print("Conveniently, Claire is the suspect's girlfriend and clears him for last night- he was home before the time of the murder.")
        item_alibi["karma"] = -10     
    elif choice == "4":
        print("Conveniently, Claire is the suspect's girlfriend and clears him for last night- he was home before the time of the murder.")         

    inventory.remove(item_warrant)
    inventory.append(item_alibi)
    calculate_karma(inventory)
    print("\n"+"The suspect has an alibi. Maybe there's more to explore back at the BAR.")
    print(item_alibi["description"])
    global current_room
    print("\n"+"You are now back in the Police Station as you have no further use for the suspect."+"\n")
    current_room = rooms["Police Station"]

def breaking_in():
    isvalid = False
    while isvalid == False:
        print("1. Break in?")
        print("2. Ask neighbour about their whereabouts")

        choice= str(input("What do you choose? Type the number."+"\n"+"> "))
        if choice =="1" or choice =="2":
            isvalid = True
        else:
            print("\n"+"That is not a valid input."+"\n")

    if choice == "1":
        print('\n' + """You force yourself in through the back door; you don't think anyone noticed. 
This place seems clean. Too clean. 
Upon looking around, you find their home telephone, it rings. 
You freeze and wait for the voicemail to click in. 
'Hi, this is Matt, I'm out of town for the next 2 months. I'll try and get back to you when I return! Sorry!'
Damn...""")
        item_proof["karma"] = -7
        item_proof["description"]= """Voicemail proving theat the suspect has been out of the country. This leaves the culprit being
only you or your partner..."""   
    elif choice == "2":
        print('\n' + """You knock on the neighbour's door to find a rather lovely little old woman, who immediately offers you
some cookies and milk. 'They're my special cookies, dear? Oh okay then. I'm sorry but you can't get a hold of Matt
for the next month and a half or so- he's gone travelling. What's this all about anyway?'
You immediately walk off... This can only mean one thing...""")
        item_proof["karma"] = 5
  

    inventory.append(item_proof)
    inventory.remove(item_car)
    print ("\n"+str(item_proof["description"]))
    global current_room
    print("\n"+"You are now back in the Housing Estate."+"\n")
    current_room = rooms["Housing Estate"]




def have_req_item(room, items):
    valid= False
    if len(rooms[room]["requireditems"]) == 3:
        valid1= False
        valid2= False
        valid3 = False
        for i in items:
            if rooms[room]["requireditems"][0] == i:
                valid1 = True
            if rooms[room]["requireditems"][1] == i:
                valid2 = True
            if rooms[room]["requireditems"][2] == i:
                valid3 = True
        if valid1== True and valid2 == True and valid3== True:
            valid= True
    elif len(rooms[room]["requireditems"]) == 2:
        valid1= False
        valid2= False
        for i in items:
            if rooms[room]["requireditems"][0] == i:
                valid1 = True
            if rooms[room]["requireditems"][1] == i:
                valid2 = True
        if valid1== True and valid2 ==True:
            valid= True
    elif len(rooms[room]["requireditems"]) ==1:
        for key in items: 
            if rooms[room]["requireditems"][0] == key:
                valid= True
    return valid

def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    global current_room 
    if is_valid_exit(current_room["exits"],direction) == True and (have_req_item(current_room["exits"][direction], inventory) == True):
        current_room=move(current_room["exits"],direction)
    
    else:
        print("\n"+"There is no reason to go there.")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    current_mass = calculate_mass(inventory)
    global karma
    found = False
    for item in current_room["items"]:
        if item["id"]== item_id:
            found= True
            itemtoadd=item
            if (current_mass+itemtoadd["mass"])>10:
                found = False
                print("You are carrying too many things.")
                break

    if found== True:
        print("You took "+str(itemtoadd["id"])+".")
        print(itemtoadd["description"])
        inventory.append(itemtoadd)
        current_room["items"].remove(itemtoadd)
        karma = calculate_karma(inventory)
        
        Continue = input("PRESS ENTER TO CONTINUE"+"\n")
        if Continue != "drtuyiop[oiuytdrtfgyhiop[oihkfcxg":
            print_room(current_room)
            print_inventory_items(inventory)

            command = menu(current_room["exits"], current_room["items"], inventory)

            execute_command(command)
        else:
            print("You cannot take that")

    
def calculate_karma(inventory):
    global karma
    karma=0
    for item in inventory:
        karma=item["karma"]+ karma
    return karma

def calculate_outcome(karma):
    gunavailable = False
    handcuffsav = False
    for item in inventory:
        if item == item_gun:
            gunavailable = True
        elif item == item_handcuffs:
            handcuffsav = True

    if karma <=0:
        print("""It's only a matter of time before your partner finds out that Matt's been out of the country. He's going to know.
I can't let him know. I need to dispose of him...""")
        if gunavailable == True:
            print("""Jack will find out. He can't find out. I need to cover my tracks. Tracks that I didn't even remember that I made.
I assumed that I made them. I mean, who else would've? Jack's far too good a cop to do this. If I'm the Back Street Butcher, then
I'm shitty enough to kill my partner. This is the day he dies. I'm sorry, Jack.
You find Jack asleep on the couch. He left the crime scene ill, earlier. He's out of it. You raise your glock to his eye socket, and pull
the trigger. He's gone.
The sound of his skull shattering reverberates around the room. It's over.""")
        elif gunavailable == False:
            print("""'I can't believe what I am. Who I am. I never would've thought my blackouts coud possibly be indicative of this.
I don't think I could live with this burden. It's too much for any one person to handle. I need to die.''
You find Jack making a cup of coffee in his kitchen. He is shocked by your presence and wonders why you are here.
Before even thinking about an answer, you tackle him to the floor. Jack quickly puts the pieces together in his head and reaches
for his pistol on his kitchen stool. You climb back to your feet and stare down at Jack...
'Do it.'
His shot echoes into the street. The killer has been stopped. You have been stopped. Your story has concluded.""")

    elif karma >0:
        print("""I don't know what possessed him, but I never did trust him. I knew he was involved in some shady shit, I should stop
him before he escapes.""")
        if gunavailable == True and handcuffsav== False:
            print("""'I've never been to his house before now; he's never invited me. No surprise after what my life has become.
Or maybe he's the one hiding things? Well, his facade has finally broken. His arrogance has got to him as he's currently
just sat on the john. Door wide open. Shit, I forgot my handcuffs- this isn't going to go well. I can't run now, he could
get away. Maybe I could claim it was self defence...'
With no remose, you unload 5 slugs into Jack's chest and watch as his empty expression slowly becomes statue. You've stopped him.""")
        elif gunavailable == False and handcuffsav== False:
            print("""'Jack always was a funny one. Very cold. A little too interested in the cases. Always understanding the killers a little too much
Creeped me right out; but I guess he always friendly enough. Maybe I can talk him out of it... He should notice that I'm unarmed, right.'
Jack wasn't in the usual friendly mood. He didn't give me a chance to ask why. He jumps on me and places his hands around my neck. 
His facial muscles don't move an inch. By contrast, my face is a screwed up mess trying to breathe in every last molecule of oxygen
that it can find. His face becomes a blur the shock subsides and I accept my fate. I was so close, yet now I am so far.
I am Jack's latest victim.""")
        elif gunavailable == True and handcuffsav == True:
            print("""'I can't believe that Jack could do this when he works for the force. I would never ever think of going against my loyalties.
I can't fathom what would bring him to do such a thing. I wonder if he can justify himself. If that's even possible.
Sarah's body was utterly brutalised. There's no rational explanation for what he did to her and her body. I've come as prepared
as I can get- I have my gun and my handcuffs. Hopefully he will see that he cannot win, he cannot go on. 
I'm going to take him down myself.'
Jack's asleep on his sofa; before he has time to react, your gun's barrel is making itself at home on his temple. He looks expasperated
as the chink of the handcuffs around his wrists signifies the hopeful end of this case and the of Jack's reign of terror.""")
    print("Congratulations. You have reached the end of the game.""")
    karma = calculate_karma(inventory)
    print("Your karma was: " + str(karma))
    print("Press enter to close.")
    end = input()
    if end != "drtuyiop[oiuytdrtfgyhiop[oihkfcxg":
        sys.exit()



def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    #for item in inventory:
    #    if item[]
    found=False

    for item in inventory:
        if item["id"]== item_id:
            found= True
            itemtodrop = item
    if found== True:
        print("You dropped "+str(itemtodrop["id"])+".")
        current_room["items"].append(itemtodrop)
        inventory.remove(itemtodrop)
    else:
        print("You cannot drop that")
    
def calculate_mass(inventory):
    mass=0
    for item in inventory:
        mass=item["mass"]+ mass
    return mass


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    if len(command) >0:
        if command[0] == "go":
            if len(command) > 1:
                execute_go(command[1])
            else:
                print("Go where?")

        elif command[0] == "take":
            if len(command) > 1:
                execute_take(command[1])
            else:
                print("Take what?")

        elif command[0] == "drop":
            if len(command) > 1:
                execute_drop(command[1])
            else:
                print("Drop what?")

        else:
            print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")
    # Normalise the input
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input



def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Robs"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    
    print()
    print(  """You peel your face off the rancid floor. 
The first pain that hits you today is coming from your knuckle; who knows what that's from. 
The second pain comes in auditory form as your phone jolts you awake. 
'Detective. Durden, it's Commissioner Sidorov, get your ass off your floor again- you're needed at 33 Park Avenue, SOUTH of MAIN STREET. ASAP. 
The Back Street Butcher has hit again. Jack's already on  his way.'""")
    print("Press enter to continue")
    # Main game loop
    global current_room
    start = input()
    if start != "drtuyiop[oiuytdrtfgyhiop[oihkfcxg":
        while True:
            print_room(current_room)
            print_inventory_items(inventory)
            if current_room== rooms["Interrogation Room"]:
                interrogation_place()
            elif current_room == rooms["Suspect's House"]:
                breaking_in()
            elif current_room == rooms["Partner's House"]:
                karma= calculate_karma(inventory)
                calculate_outcome(karma)
            elif current_room == rooms["Lab"]:
                inventory.append(item_blood)
                inventory.remove(item_jumper)
                current_room = rooms["Police Station"]
                print(item_blood["description"])
                print("You return to the Police Station."+"\n")
            elif current_room == rooms["Claire's Office"]:
                for item in inventory:
                    if item == item_blood:
                        if item == item_warrant:
                            inventory.remove(item_blood)
                            rooms["Claire's Office"]["requireditems"] = []

            

            for item in inventory:
                if item["name"] == item_car["name"]:
                    rooms["Suspect's House"]["isvisible"]= True
                elif item["name"] == item_alibi["name"]:
                    rooms["CCTV Room"]["isvisible"]= True
                elif item["name"] == item_beer["name"]:
                    rooms["Bar"]["isvisible"]= True
                elif item["name"] == item_proof["name"]:
                    rooms["Partner's House"]["isvisible"]= True
            command = menu(current_room["exits"], current_room["items"], inventory)

            execute_command(command)
    


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

