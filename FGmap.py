from fgitems import *

your_flat = {
    "name": "Your flat",

    "description":
    """You are in your flat. It's a dingy place, 
with peculiar looking beer bottles strewn across the place.
It smells like it hasn't been cleaned in months; 
it looks like it hasn't been cleaned in years. But it's home, nonetheless.""",

    "exits": {"west": "Housing Estate"},


    "items": [item_gun, item_handcuffs, item_badge],
    "requireditems":[item_badge]

}

the_hub = {
    "name": "Main Street",

    "description":
    """You are in the centre of town, the whole world is at your fingertips. 
And by whole world, I mean a few select locations within New York.""",

    "exits":  {"north": "Housing Estate", "south": "Crime Scene", "east": "Police Station", "west": "Bar"},


    "items": [],
    "requireditems":[item_badge]

}

crime_scene = {
    "name": "Crime Scene",

    "description":
    """You are confronted with a brutal sight: the body absorbs all of the
happiness that may have existed here. The smell is already pungent- however,
the most perplexing aspect is the body's attire... They appear to be wearing a
men's jumper.""",

    "exits": {"north": "Main Street"},


    "items": [item_jumper, item_handbag, item_watch, item_beer],
    "requireditems":[item_badge]

}

police_station = {
    "name": "Police Station",

    "description":
    """You are awkwardly standing at the desk of your coworker, Claire. 
She might help you get people in for questioning if you're lucky.""",

    "exits": {"west": "Main Street", "south": "Interrogation Room", "north": "Lab"},


    "items": [item_warrant],
    "requireditems":[item_badge]


}

room_bar = {
    "name": "Bar",

    "description":
    """You are standing at the bar, trying to not to throw up 
as it happens to smell approximately like a toilet
- specifically, your toilet after last night. The barman looks at you inquisitively.""",

    "exits": {"east": "Main Street", "west": "CCTV Room"},


    "items": [],
    "requireditems":[item_badge]

}

CCTV_room = {
    "name": "CCTV Room",

    "description":
    """This room hasn't been properly staffed in a while- it's a mess.
Luckily, their equipment has still been running and they haven't ran out of tape yet.
Maybe you can find something on the tape of last night.""",

    "exits": {"east": "Bar"},

    "items": [item_carInformation],
    "requireditems":[item_alibi]

}
suspect_house = {
    "name": "Suspect's House",

    "description":
    """You arrive at the front door of the house. 
You can hear music pumping from the neighbour's house. 
You may knock on the door; there is, however, a first floor window open...""",

    "exits": {"south": "Housing Estate"},

    "items": [item_proof],
    "requireditems":[item_carInformation]

}

room_lab = {
    "name": "Lab",

    "description":
    """You find yourself acquianted with Dexter, his ginger hair lights up the room.
His cold, apathetic look almost unnerves you, but he seems happy to help.""",

    "exits": {"south": "Police Station"},

    "items": [item_blood],
    "requireditems":[item_jumper]
}

interrogation_room = {
    "name": "Interrogation Room",

    "description":
    """You are sat opposite a rather dashing looking feller, 
who calmly welcomes your presence with a smile. 
His arrogant facade might be hiding something.""",

    "exits": {"north": "Police Station"},

    "items": [item_alibi],
    "requireditems":[item_warrant]
}

partners_house = {
    "name": "Partner's House",

    "description":
    """This house is nice. Really nice. Beats your shoddy excuse for flat; 
not that that says much. Maybe you'll live somewhere like here one day.""",

    "exits": {"east": "Housing Estate"},

    "items": [],
    "requireditems":[item_proof]
}

housing_estate = {
    "name": "Housing Estate",

    "description":
    """Your luxurious motor vehicle looks somewhat out of place 
against this backdrop of alcoholics, thugs, and prostitutes.""",

    "exits": {"south": "Main Street", "east": "Your Flat", "north": "Suspect's House", "west": "Partner's House"},

    "items": [],
    "requireditems":[item_badge]

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
    "Bar": room_bar,
    "Partner's House": partners_house,
    "Housing Estate": housing_estate
}
