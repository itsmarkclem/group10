from fgitems import *

your_flat = {
    "name": "Your flat",

    "description":
    """You are in your flat. It's a dingy place, 
with peculiar looking beer bottles strewn across the place.
It smells like it hasn't been cleaned in months; 
it looks like it hasn't been cleaned in years. But it's home, nonetheless.""",

    "exits": {"out": "Main Street"},

    "items": [item_gun, item_handcuffs, item_badge]
}

the_hub = {
    "name": "Main Street",

    "description":
    """You are in the centre of town, the whole world is at your fingertips. 
And by whole world, I mean a few select locations within New York.""",

    "exits":  {"north": "Suspect's House", "south": "Crime Scene", "east": "Police Station", "west": "Pub", "southeast": "Partner's House", "northwest": "Suspect Two's House", "northeast": "Your flat"},

    "items": []
}

crime_scene = {
    "name": "Crime Scene",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    "exits": {"north": "Main Street"},

    "items": [item_jumper, item_handbag, item_watch, item_beer]
}

police_station = {
    "name": "Police Station",

    "description":
    """You are awkwardly standing at the desk of your coworker, Claire. 
She might help you get people in for questioning if you're lucky.""",

    "exits": {"west": "Main Street", "south": "Interrogation room", "north": "Lab"},

    "items": [item_carInformation, item_warrant]
}

room_bar = {
    "name": "Bar",

    "description":
    """You are standing at the bar, trying to not to throw up 
as it happens to smell approximately like a toilet
- specifically, your toilet after last night. The barman looks at you inquisitively.""",

    "exits": {"east": "Main Street", "west": "CCTV Room"},

    "items": []
}

CCTV_room = {
    "name": "CCTV Room",

    "description":
    """This room hasn't been properly staffed in a while- it's a mess.
Luckily, their equipment has still been running and they haven't ran out of tape yet.
Maybe you can find something on the tape of last night.""",

    "exits": {"east": "Pub"},

    "items": [item_cctvTapes]
}

suspect_house = {
    "name": "Suspect's House",

    "description":
    """You arrive at the front door of the house. 
You can hear music pumping from the neighbour's house. 
You may knock on the door; there is, however, a first floor window open...""",

    "exits": {"south": "Main Street",},

    "items": []
}

room_lab = {
    "name": "Lab",

    "description":
    """You find yourself acquianted with Dexter, his ginger hair lights up the room.
His cold, apathetic look almost unnerves you, but he seems happy to help.""",

    "exits": {"south": "Police Station"},

    "items": [item_DNA]
}

interrogation_room = {
    "name": "Interrogation Room",

    "description":
    """You are sat opposite a rather dashing looking feller, 
who calmly welcomes your presence with a smile. 
His arrogant facade might be hiding something.""",

    "exits": {"north": "Police Station"},

    "items": []
}


rooms = {
    "Main Street": the_hub,
    "Your Flat": your_flat,
    "Crime Scene": crime_scene,
    "Police Station": police_station,
    "Lab": room_lab,
    "Interrogation Room": interrogation_room,
    "Suspect's House": suspect_house,
    "CCTV Room": CCTV_room,
    "Bar": room_bar
}
