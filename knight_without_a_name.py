import time

# Delay print & logo
def print_slow(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

time.sleep(1)
print() 
print_slow("░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
print_slow("░░░░𝕶 ░𝖓 ░𝖎 ░𝖌 ░𝖍 ░𝖙 ░░░░░\n")
print_slow("░░░𝖜 ░𝖎 ░𝖙 ░𝖍 ░𝖔 ░𝖚 ░𝖙 ░░░\n")
print_slow("░░░░░𝖆 ░░░𝖓 ░𝖆 ░𝖒 ░𝖊 ░░░░░\n")
print_slow("░░░░░░░░░░░░░░░░░░░░░░░░░░\n")

# Inventory
inventory = ["sword"]

# Items
items = {
    "lamp": {
        "desc": "An old brass lamp that provides light. Gothic in style, with intricate engravings.",
    },
    "rusty key": {
        "desc": "A rusty key. It looks very old. I wonder what it opens?",
    },
    "bone": {
        "desc": "A large bone from the humanoid skeleton 𝕷𝖔𝖗𝖉 𝕸𝖆𝖗𝖗𝖔𝖜𝖛𝖊𝖎𝖑. I bet a dog would love this.",
    },
    "usb stick": {
        "desc": "A small USB flash drive with a plain black casing. It might contain files useful for the office computer.",
    },
    "sword": {
        "desc": "A sharp looking sword with the blade glinting in the light, and intricate engravings on the hilt.\nThe craftsmanship is exquisite. There's a poem engraved on the blade:\n'𝕿𝖍𝖗𝖔𝖚𝖌𝖍 𝖗𝖚𝖎𝖓𝖘 𝖈𝖔𝖑𝖉, 𝕴 𝖜𝖆𝖑𝖔𝖓𝖊\n𝕬𝖘𝖍𝖊𝖘 𝖋𝖆𝖑𝖑 𝖑𝖎𝖐𝖊 𝖘𝖓𝖔𝖜 𝖔𝖓 𝖘𝖜𝖔𝖗𝖉\n𝕹𝖔 𝖋𝖑𝖆𝖌 𝖗𝖆𝖎𝖘𝖊𝖉, 𝖓𝖔 𝖛𝖔𝖎𝖈𝖊 𝖙𝖔 𝖈𝖆𝖑𝖑\n𝕵𝖚𝖘𝖙 𝖇𝖑𝖔𝖔𝖉 𝖆𝖓𝖉 𝖛𝖎𝖔𝖑𝖊𝖓𝖈𝖊 — 𝖙𝖍𝖆𝖙 𝖎𝖘 𝖆𝖑𝖑.'",
    },
}

# Drop Item
def drop_item(item: str, room_items: list, inventory: list) -> bool:
    if item in inventory:
        inventory.remove(item)
        room_items.append(item)
        print(f"\nYou dropped the {item}.\n")
        return True
    else:
        print(f"\nYou don't have a {item} to drop.\n")
        return False


# NPC
npcs = {
    "dog": {
        "desc": "A black dog with one of its ears missing. Perhaps a Lapphund?\nIts eyes are sharp and intelligent and you can tell it has seen things.",
    },
    "skeleton": {
        "desc": "A humanoid skeleton, clad in tattered remnants of armor. It stands motionless, its empty eye sockets staring into the void.\nEngraved on the breastplate are the words: '𝕷𝖔𝖗𝖉 𝕸𝖆𝖗𝖗𝖔𝖜𝖛𝖊𝖎𝖑'.",
    },
}

# Show Inventory
def show_inventory():
    if inventory:
        print("\nYour inventory contains:")
        for item in inventory:
            print(f"  - {item}")
    else:
        print("\nYour inventory is empty.")
    print()

# Examine Item
def examine_item(item: str, room_items=None) -> None:

    if item in npcs:
        examine_npc(item)
        return
    
    if item in items:
        print(f"\n{items[item]['desc']}\n")
        return

    if (room_items and item in room_items) or (item in inventory):
        print(f"\nYou see a {item}.\n")
        return

    print(f"\nThere is no {item} here or in your inventory.\n")

# Take Item
def take_item(item, room_items, inventory):
    if item in room_items:
        inventory.append(item)
        room_items.remove(item)
        return True
    return False

# Examine / Look / Use NPC
def examine_npc(npc_name):
    if npc_name in npcs:
        print("\n" + npcs[npc_name]['desc'] + "\n")
    else:
        print(f"\nThere is no {npc_name} here.\n")

# Quit Game
def handle_quit():
    confirm = input("\nAre you sure you want to quit? (𝖞𝖊𝖘/𝖓𝖔): ").lower().strip()
    if confirm in ("yes"):
        print("\n𝕰𝖝𝖎𝖙𝖎𝖓𝖌 𝖙𝖍𝖊 𝖌𝖆𝖒𝖊...")
        time.sleep(3)
        exit()
    else:
        print("\n𝕮𝖔𝖓𝖙𝖎𝖓𝖚𝖎𝖓𝖌 𝖞𝖔𝖚𝖗 𝖆𝖉𝖛𝖊𝖓𝖙𝖚𝖗𝖊...\n")

# Help Menu
def help_menu():
    print("\nAvailable commands:")
    print("  - Directions: north(n), south(s), east(e), west(w)")
    print("  - Actions: look, examine, talk to [npc], use [item], take [item], drop [item], inventory")
    print("  - Other: help, quit, exit\n")

# Room access
room_9_open = True
room_13_open = True

# Room 1 / Dungeon Entrance
def room_1():
    room_items = []
    print("\nYou see the entrance to a dungeon located between two tall mountains. It looks dark and foreboding.")
    print("You can go *north* to head inside the dungeon, or *south* to leave.")
    print("What will you do?\n")
    
    while True:
        choice = input("░ ").lower().strip()

        if choice in ("n", "north", "go north"):
            room_5()
            break
        elif choice in ("s", "south", "go south"):
            room_2()
            break
        elif choice in ("look", "examine") or choice.startswith("examine ") or choice.startswith("look "):
            if choice in ("look", "examine"):
                print("\nThe dungeon entrance is made of ancient megalithic stone, covered in moss and vines.")
                print("The pillars are towering above you, casting long shadows.")
                print("Each pillar has a sculptured face, worn by time but still discernible.")
                print("There's a barely visible engraving above the entrance that reads: '𝕵.𝕿. 𝕸 𝕸 𝖃 𝖃 𝖁'.\n")
            else:
                target = choice.split(" ", 1)[1]
                examine_item(target, room_items)
        elif choice.startswith("drop "):
            item = choice[5:]
            drop_item(item, room_items, inventory)
        elif choice in ("inventory", "i"):
            show_inventory()
        elif choice in ("help"):
            help_menu()
        elif choice in ("quit", "exit"):
            handle_quit()
        else:
            print("\nI don't understand.\n")

# Room 2 / Forest
def room_2():
    room_items = []
    print("\nYou enter a dense, tangled forest.")
    print("There is a thin wisp of smoke rising behind the trees to the *west*, and you can hear a waterfall flowing to the *east*.")
    print("The dungeon entrance is located *north* of your current location.")
    print("What will you do?\n")

    while True:
        choice = input("░ ").lower().strip()

        if choice in ("w", "west", "go west"):
            room_3()
            break
        elif choice in ("e", "east", "go east"):
            room_4()
            break
        elif choice in ("n", "north", "go north"):
            room_1()
            break
        elif choice in ("look", "examine") or choice.startswith("examine ") or choice.startswith("look "):
            if choice in ("look", "examine"):
                print("\nThe forest is a mix of tall pine trees and ancient oaks, their branches forming a dense canopy overhead.")
                print("The wind rustles the leaves, creating a soothing whispering sound. It feels peaceful here.")
                print("You can smell the scent of pine and earth.\n")
            else:
                target = choice.split(" ", 1)[1]
                examine_item(target, room_items)
        elif choice.startswith("drop "):
            item = choice[5:]
            drop_item(item, room_items, inventory)
        elif choice in ("inventory", "i"):
            show_inventory()
        elif choice in ("help"):
            help_menu()
        elif choice in ("quit", "exit"):
            handle_quit()
        else:
            print("\nI don't understand.\n")

# Room 3 / The Hollow Shield Inn
def room_3():
    room_items = ["bone"] if "sword" not in inventory and "bone" not in inventory else []
    print("\nThe forest opens up into a small clearing.")
    print("Before you stands a weathered timber inn, its dark oak beams bent with age.")
    print("A crooked sign hangs from rusted chains above the door.")
    print("It bears the image of a circular wooden shield with a single arrow piercing through it in a diagonal angle.")
    print("The barely readable inscription reads: '𝕿𝖍𝖊 𝕳𝖔𝖑𝖑𝖔𝖜 𝕾𝖍𝖎𝖊𝖑𝖉 𝕴𝖓𝖓'. You open the door and step inside.")
    print("If you want to leave, you can go *east* back into the forest.")
    print("What will you do?\n")
    
    while True:
        choice = input("░ ").lower().strip()

        if choice in ("e", "east", "go east"):
            room_2()
            break
        elif choice in ("look", "examine") or choice.startswith("examine ") or choice.startswith("look "):
            if choice in ("look", "examine"):
                print("\nA long counter of age-darkened wood stretches along the back wall, its surface scarred with initials and the marks of countless knife games.\nBehind it, shelves sag under the weight of dusty bottles and ancient tankards. Some bottles contain murky liquids that haven't been touched in years.\nNo one stands behind the bar. No one tends this place.")
                print("In the corner, next to the fireplace, a dog is lying down.\n")
                if "sword" in inventory:
                    print("It eyes you with a mix of curiosity and judgment.\n")
            else:
                target = choice.split(" ", 1)[1]
                examine_item(target, room_items)
        elif choice in ("use dog", "talk to dog", "pet dog"):
            if "sword" in inventory:
                print("\nThe dog growls lowly, baring its teeth a little. It seems wary of you.\n")
            else:
                print("\nYou kneel down to the dog's level, extending a hand slowly.")
                print("The dog sniffs your hand cautiously, lets out a low growl, then leans in for a gentle nuzzle.")
                print("It seems to appreciate the attention.\n")
        elif choice in ("look dog", "examine dog"):
            examine_npc("dog")
            if "bone" in inventory:
                print("There seems to be a key of some kind beneath where the dog is lying.")
                print("I wonder if the animal takes bribes?\n")
            if "rusty key" in inventory:
                print("The dog seems to be resting peacefully now next to the bone.")
                print("It's almost as if it's smiling at you.\n")
            else:
                print("There's something beneath the dog, but it won't let you near it.\n")
        elif choice in ("use bone", "give bone", "offer bone"):
            if "bone" not in inventory:
                print("\nYou don't have a 𝖇𝖔𝖓𝖊 to give.\n")
            else:
                print("\nYou offer the 𝖇𝖔𝖓𝖊 to the dog.")
                time.sleep(5)
                print(r"""
         _                  
        / `-.              
       |  ,-.`-.         
       \  :  `. `.       ,'-. 
        \ ;    ;  `-.__,'    `-.
         \ ;   ;  :::  ,::'`:.  `. 
          \ `-. :  `    :.    `.  \ 
           \   \    ,   ;   ,:    (\ 
            \   :., :.    ,'∅)): ` `-. 
           ,/,' ;' ,::"'`.`---'   `.  `-._ 
         ,/  :  ; '"      `;'          ,--`. 
        ;/   :; ;             ,:'     (   ,:) 
          ,.,:.    ; ,:.,  ,-._ `.     \""'/ 
          '::'     `:'`  ,'(  \`._____.-'"' 
             ;,   ;  `.  `. `._`-.  \\       ░ bork.
             ;:.  ;:       `-._`-.\  \`. 
              '`:. :        |' `. `\  ) \ 
                ` ;:       |    `--\__,' 
                   '`      ,' 
                        ,-' """)
            
                print("\nThe dog's eyes light up, and it takes the bone gently from your hand.")
                print("It wags its tail a little and seems to warm up to you.")
                inventory.remove("bone")
                room_items.append("rusty key")
                print("As the dog moves to chew the 𝖇𝖔𝖓𝖊, a 𝖗𝖚𝖘𝖙𝖞 𝖐𝖊𝖞 is revealed where it was lying.")
                print("What will you do?\n")
        elif choice.startswith("take "):
            item = choice[5:]
            if "rusty key" in room_items and item == "rusty key":
                if take_item(item, room_items, inventory):
                    print(f"\nYou took the {item}.\n")
            else:
                print(f"\nThere is no {item} here to take.\n")
        elif choice.startswith("drop "):
            item = choice[5:]
            drop_item(item, room_items, inventory)
        elif choice in ("inventory", "i"):
            show_inventory()
        elif choice in ("help"):
            help_menu()
        elif choice in ("quit", "exit"):
            handle_quit()
        else:
            print("\nI don't understand.\n")

# Room 4 / River
def room_4():
    room_items = ["usb stick"] if "usb stick" not in inventory else []
    print("\nYou arrive at the shore of a wide river.")
    print("There is a small canoe tied to a post on the shore. It looks old and weathered, but it might still be usable.")
    print("You can take the canoe downstream to the *south*. You can also go back to the forest to the *west*.")
    print("What will you do?\n")
    
    while True:
        choice = input("░ ").lower().strip()

        if choice in ("w", "west", "go west"):
            room_2()
            break
        elif choice in ("s", "south", "go south"):
            print("\nYou carefully step into a small canoe tied to the shore.")
            print("Using the oar, you begin to row downstream, the current aiding your progress.")
            print("As you navigate the river, the speed of the water increases, and you start to hear the roar of the waterfall growing louder.")
            print("There's water leaking into the canoe. You start to panic.")
            print("Suddenly, the canoe is swept over the edge of the waterfall.")
            print("𝕲𝖆𝖒𝖊 𝖔𝖛𝖊𝖗...\n")
            time.sleep(10)
            exit()
            break
        elif choice in ("look", "examine") or choice.startswith("examine ") or choice.startswith("look "):
            if choice in ("look", "examine"):
                print("\nThe water rushes past you with a powerful current, creating a soothing roar.")
                print("A waterfall cascades down from a cliff further upstream, creating a misty spray that obscures your vision.")
                print("The river is wide and fast-flowing, its surface shimmering in the light.")
                print("Upon closer inspection, the canoe appears to have a small hole in the bottom.")
                if "usb stick" in room_items:
                    print("There's something small and black caught between the rocks near the shore; it appears to be a USB stick.\n")
                else:
                    print()
            else:
                target = choice.split(" ", 1)[1]
                examine_item(target, room_items)
        elif choice.startswith("take "):
            item = choice[5:]
            if take_item(item, room_items, inventory):
                print(f"\nYou took the {item}.\n")
            else:
                print(f"\nThere is no {item} here to take.\n")
        elif choice.startswith("drop "):
            item = normalize_item(choice[5:])
            drop_item(item, room_items, inventory)
        elif choice in ("inventory", "i"):
            show_inventory()
        elif choice in ("help"):
            help_menu()
        elif choice in ("quit", "exit"):
            handle_quit()
        else:
            print("\nI don't understand.\n")

# Room 5 / Dungeon Lobby
def room_5():
    room_items = []
    print("\nYou enter a cold stone hall. It\'s dark and damp.")
    print("There are two passages in front of you: one to the *west* and another to the *east*.")
    print("You can also return outside the dungeon, to the *south*.")
    print("What will you do?\n")

    while True:
        choice = input("░ ").lower().strip()

        if choice in ("e", "east", "go east"):
            room_6()
            break
        elif choice in ("w", "west", "go west"):
            room_7()
            break
        elif choice in ("s", "south", "go south"):
            room_1()    
            break
        elif choice in ("look", "examine") or choice.startswith("examine ") or choice.startswith("look "):
            if choice in ("look", "examine"):
                print("\nThe hall is lined with ancient stone pillars, spiraling upwards towards the darkness above.")
                print("Cobwebs hang from the corners, and the air is thick with the smell of damp earth and mold.")
                print("The space is large and foreboding.\n")
            else:
                target = normalize_item(choice.split(" ", 1)[1])
                examine_item(target, room_items)
        elif choice.startswith("drop "):
            item = normalize_item(choice[5:])
            drop_item(item, room_items, inventory)
        elif choice in ("inventory", "i"):
            show_inventory()
        elif choice in ("help"):
            help_menu()
        elif choice in ("quit", "exit"):
            handle_quit()
        else:
            print("\nI don't understand.\n")

# Room 6 / The Silent Cavern
def room_6():
    room_items = ["lamp"] if "lamp" not in inventory else []

    print("\nYou enter a cavernous chamber.")
    print("The walls are rough and jagged, with stalactites hanging from the ceiling.")
    print("You can go *south* to go deeper into the dungeon.")
    print("There is a faint light coming from *west*, where the dungeon lobby is located.")
    print("What will you do?\n")

    while True:
        choice = input("░ ").lower().strip()

        if choice in ("w", "west", "go west"):
            room_5()
            break
        elif choice in ("s", "south", "go south"):
            room_8()
            break
        elif choice in ("look", "examine") or choice.startswith("examine ") or choice.startswith("look "):
            if choice in ("look", "examine"):
                print("\nThe cavern is vast and echoing and you can barely make out the walls in the dim light.")
                print("The air feels heavy. Something is lurking just out of sight.\n")
                if any(item == "lamp" for item in room_items):
                    print("You see an old 𝖑𝖆𝖒𝖕 in the corner, with shadows dancing around it.\n")
            else:
                target = choice.split(" ", 1)[1]
                examine_item(target, room_items)
        elif choice.startswith("take "):
            item = choice[5:]
            if take_item(item, room_items, inventory):
                print(f"\nYou took the {item}.\n")
            else:
                print(f"\nThere is no {item} here to take.\n")        
        elif choice.startswith("drop "):
            item = choice[5:]
            drop_item(item, room_items, inventory)
        elif choice in ("inventory", "i"):
            show_inventory()
        elif choice in ("help"):
            help_menu()
        elif choice in ("quit", "exit"):
            handle_quit()
        else:
            print("\nI don't understand.\n")

# Room 7 / The Carved Corridor
def room_7():
    room_items = []
    print("\nYou arrive into a narrow corridor.")
    print("The walls are lined with ancient stone carvings, depicting scenes of battles long past.")
    print("You can go *north* or *south*, deeper into the dungeon.")
    print("There is a passage to the *east* leading back to the dungeon lobby.")
    print("What will you do?\n")

    while True:
        choice = input("░ ").lower().strip()

        if choice in ("e", "east", "go east"):
            room_5()
            break
        elif choice in ("s", "south", "go south"):
            print("\nSuddenly the floor below you opens, and you start falling in to the void.") 
            print("You die weeks later, still falling in nothingness.")
            print("𝕲𝖆𝖒𝖊 𝖔𝖛𝖊𝖗...\n")
            time.sleep(10)
            exit()
            break
        elif choice in ("n", "north", "go north"):
            if room_9_open:
                room_9()
                break
            else:
                print("\nThe northern passage is blocked; you can't go that way anymore.\n")
        elif choice in ("look", "examine") or choice.startswith("examine ") or choice.startswith("look "):
            if choice in ("look", "examine"):
                print("\nThe corridor is narrow and dimly lit, with flickering torches casting long shadows on the walls.")
                print("The stone carvings are worn with age, but you can still make out the details of the battles they depict.\n")
            else:
                target = choice.split(" ", 1)[1]
                examine_item(target, room_items)
        elif choice.startswith("drop "):
            item = choice[5:]
            drop_item(item, room_items, inventory)
        elif choice in ("inventory", "i"):
            show_inventory()
        elif choice in ("help"):
            help_menu()
        elif choice in ("quit", "exit"):
            handle_quit()
        else:
            print("\nI don't understand.\n")

# Room 8 / The Forgotten Catacombs
def room_8():
    room_items = []
    print("\nYou descend into an eerie catacomb.")
    print("The air is thick with the scent of decay, and the walls are lined with ancient bones.")
    print("You can go back towards the dungeon lobby to the *west*, or venture further into the catacombs to the *east*.")
    print("There seems a way forward to the *north* as well, but it looks treacherous.")
    print("What will you do?\n")
    while True:
        choice = input("░ ").lower().strip()

        if choice in ("w", "west", "go west"):
            room_6()
            break
        elif choice in ("n", "north", "go north"):
            print("\nYou venture deeper into the catacombs, but soon find yourself lost in a maze of tunnels.")
            print("After wandering for what feels like hours, you realize you're hopelessly lost.")
            print("You sit down like Jack Torrance in the maze, waiting for the end to come.")
            print("𝕲𝖆𝖒𝖊 𝖔𝖛𝖊𝖗...\n")
            time.sleep(10)
            exit()
            break
        elif choice in ("e", "east", "go east"):
            room_10()
            break
        elif choice in ("look", "examine") or choice.startswith("examine ") or choice.startswith("look "):
            if choice in ("look", "examine"):
                print("\nThe catacombs are dark and foreboding, with walls lined with the skeletal remains of long-dead inhabitants.")
                print("The air is damp and musty, and you can hear the faint sound of dripping water echoing through the tunnels.\n")
            else:
                target = choice.split(" ", 1)[1]
                examine_item(target, room_items)
        elif choice.startswith("drop "):
            item = choice[5:]
            drop_item(item, room_items, inventory)
        elif choice in ("inventory", "i"):
            show_inventory()
        elif choice in ("help"):
            help_menu()
        elif choice in ("quit", "exit"):
            handle_quit()
        else:
            print("\nI don't understand.\n")

# Room 9 / The Obsidian Chamber
def room_9():
    global room_9_open
    room_items = []
    if "sword" in inventory:
            print("\nYou venture countless tunnels and finally enter a dimly lit chamber.")
            print("The space is perfectly circular, with walls made of obsidian stone that seem to absorb all light.")
            print("In the center stands a skeleton. It doesn't seem to notice your presence.")
            print("You can return to the carved corridor to the south.")
    else:
        print("\nYou cautiously enter the obsidian chamber.")
        print("The skull of the defeated skeleton grins up at you, your sword still lodged in it.")
        print("There is a strangely symmetrical bone next to it.")
        print("You can return to the carved corridor to the south.")
    print("What will you do?\n")

    while True:
        choice = input("░ ").lower().strip()
        room_items = ["bone"] if "sword" not in inventory and "bone" not in inventory else []

        if choice in ("s", "south", "go south"):
            if "bone" in inventory and room_9_open:
                room_9_open = False
                print("\nThe ground starts to tremble as you turn to leave the chamber. Bones start to rain down from the ceiling.")
                time.sleep(5)
                print("You barely make it out before the passage collapses behind you, sealing it forever.")
            room_7()
            break
        elif choice in ("look", "examine") or choice.startswith("examine ") or choice.startswith("look "):
            if choice in ("look", "examine"):
                print("\nThe obsidian walls are smooth and cold to the touch, reflecting your image in a distorted manner.")
                print("The chamber is eerily silent, with an oppressive atmosphere that weighs heavily on your mind.")
                print("There are bones scattered across the floor. Must be remnants of past adventurers who met their end here.\n")
            else:
                target = choice.split(" ", 1)[1]
                examine_item(target, room_items)
        elif choice in ("talk to skeleton", "speak to skeleton"):
            if "sword" in inventory:
                print("\nThe skeleton's jaw creaks open, and it speaks in a hollow voice like from a great distance:\n'I've been waiting for you, 𝖓𝖆𝖒𝖊𝖑𝖊𝖘𝖘 𝖔𝖓𝖊...'\n")
        elif choice in ("look skeleton","use skeleton", "examine skeleton"):
            if "sword" in inventory:
                examine_npc("skeleton")
                print("You feel a sudden urge for a bit of the old ultraviolence.\n")    
        elif choice in ("use sword"):
            if "sword" in inventory:
                print("\nYou pull out your 𝖘𝖜𝖔𝖗𝖉, gripping it tightly as you face the skeleton.")
                time.sleep(5)
                print(r"""    
                                   ,--.
                                  {    }
                                  K,   }
                                 /  ~Y`
                            ,   /   /
                           {_'-K.__/
                             `/-.__L._
                             /  ' /`\_}
                            /  ' /
                    ____   /  ' /
             ,-'~~~~    ~~/  ' /_
           ,'             ``~~~  ',
          (                        Y
         {                         I
        {      -                    `,
        |       ',                   )
        |        |   ,..__      __. Y
        |    .,_./  Y ' / ^Y   J   )|
        \           |' /   |   |   ||
         \          L_/    . _ (_,.'(
          \,   ,      ^^""' / |      )
            \_  \          /,L]     /
              '-_~-,       ` `   ./`      ░ clonk.
                 `'{_            )
                     ^^\..___,.--` """)

                print("\nWith a swift motion, you strike at the skeleton.\nThe blade cuts through the air, and the skeleton shatters to the obsidian floor in a shower of bones.")
                print("Your 𝖘𝖜𝖔𝖗𝖉 is stuck in the skeleton's head.")
                inventory.remove("sword")
                room_items.append("bone")
                print("Among the remains of the skeleton, you find a strangely symmetrical 𝖇𝖔𝖓𝖊.")
                print("What will you do?\n")
        elif choice.startswith("take "):
            item = choice[5:]
            if "bone" in room_items and item == "bone":
                if take_item(item, room_items, inventory):
                    print(f"\nYou took the {item}.\n")
            else:
                print(f"\nThere is no {item} here to take.\n")
        elif choice.startswith("drop "):
            item = choice[5:]
            drop_item(item, room_items, inventory)
        elif choice in ("inventory", "i"):
            show_inventory()
        elif choice in ("help"):
            help_menu()
        elif choice in ("quit", "exit"):
            handle_quit()
        else:
            print("\nI don't understand.\n")

# Room 10 / The Throne Room
def room_10():
    room_items = []
    print("\nYou step into a grand throne room, its walls adorned with faded tapestries and ancient banners.")
    print("At the far end of the room sits a massive throne, carved from dark stone and encrusted with jewels.")
    print("There is a passage behind the throne, leading *south*. The catacombs lie to the *west*.")
    print("What will you do?\n")

    while True:
        choice = input("░ ").lower().strip()

        if choice in ("w", "west", "go west"):
            room_8()
            break
        elif choice in ("s", "south", "go south"):
            room_11()
            break
        elif choice in ("look", "examine") or choice.startswith("examine ") or choice.startswith("look "):
            if choice in ("look", "examine"):
                print("\nThe throne room is vast and empty, with high ceilings and grand arches.")
                print("The throne itself is imposing, with intricate carvings of mythical creatures and ancient symbols.")
                print("Dust motes dance in the shafts of light that filter through the cracked windows.\n")
            else:
                target = choice.split(" ", 1)[1]
                examine_item(target, room_items)
        elif choice.startswith("drop "):
            item = choice[5:]
            drop_item(item, room_items, inventory)
        elif choice in ("inventory", "i"):
            show_inventory()
        elif choice in ("help"):
            help_menu()
        elif choice in ("quit", "exit"):
            handle_quit()
        else:
            print("\nI don't understand.\n")

# Room 11 / Dark Corridor
def room_11():
    room_items = []
    print("\nYou enter a narrow and pitch black corridor. It feels cold here.")
    if "lamp" not in inventory:
        print("It's pitch black. You can't see anything without a light source.")
        print("You can return to the throne room to the *north*.")
    elif "rusty key" not in inventory:
        print("You hold up the 𝖑𝖆𝖒𝖕, illuminating a heavy door with rusty lock and a small window.")
        print("You can return to the throne room to the *north*.")
    else:
        print("You hold up the 𝖑𝖆𝖒𝖕, illuminating a heavy door with rusty lock and a small window.")
        print("You can return to the throne room to the *north*.")
    print("What will you do?\n")
    
    while True:
        choice = input("░ ").lower().strip()

        if choice in ("n", "north", "go north"):
            room_10()
            break
        elif choice in ("look", "examine"):
            if "lamp" not in inventory:
                print("\nIt's too dark to see anything.\n")
            elif "rusty key" not in inventory:
                print("\nThe lamp reveals some kind of chamber on the other side of the door, but it's locked tight.\n")
            else:
                print("\nThe lamp reveals some kind of chamber on the other side of the door. The rusty key in your pocket might fit.\n")
        elif choice in ("use lamp", "light lamp"):
            if "lamp" in inventory:
                print("\nYou're already using the 𝖑𝖆𝖒𝖕 to light the area.\n")
            else:
                print("\nYou don't have a 𝖑𝖆𝖒𝖕.\n")
        elif choice in ("use key", "use rusty key", "unlock", "unlock door"):
            if "rusty key" in inventory:
                if "lamp" in inventory:
                    time.sleep(3)
                    print(r"""
        .._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..
           `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  
              | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  
        ..__  |     |`-!._ | `.| |_______░_______||."'|  _!.;'   |     _|..
           |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    
           |      |``--..|_ | `;!|░|MMoMMMMoMMM|░|.'j   |_..!-'|     |     
           |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     
        ___|______|____!.,.!,.!,!|░|MMMo * loMM|░|,!,.!.,.!..__|_____|_____
              |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  
              |     |    |..!-;'i|░|MPYMoMMMMoM|░| |`-..|   |    |      |  
              |    _!.-j'  | _!,"|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  
             _!.-'|    | _."|  !;|░|MbdMMoMMMMM|░|`.| `-._|    |``-.._  |  
        ..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..
           |      |.|    |.|  !| |░|MoMMMMoMMMM|░||`. |`!   | `".    |     
           |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     
          _!"'|     !.'|  .'| .'|[░]MMMMMMMMMMM[░] \|  `. | `._  |   `-._  
        -'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-
              |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  
             .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  
          _.'     !'|   .' | /                       \|  `  |  `.    |`.|  """)
                    print("\nYou insert the 𝖗𝖚𝖘𝖙𝖞 𝖐𝖊𝖞 into the lock. It fits and the door creaks open...")
                    print("You step in.\n")
                    room_12()
                    break
            elif "lamp" not in inventory:
                print("\nIt's too dark to find the keyhole.\n")
            else:
                print("\nYou don't have the right 𝖐𝖊𝖞.\n")
        elif choice.startswith("drop "):
            item = choice[5:]
            drop_item(item, room_items, inventory)        
        elif choice in ("inventory", "i"):
            show_inventory()
        elif choice == "help":
            help_menu()
        elif choice in ("quit", "exit"):
            handle_quit()
        else:
            print("\nI don't understand.\n")
                    
# Room 12 / Server Room
def room_12():
    room_items = []
    print("You enter a server room of some kind.")
    print("The air is cool and humming with the sound of unseen machinery.")
    print("You can see a set of concrete stairs going up towards *south*.")
    print("Door with a small, circular plate etched with the word 'W.C.' is to the *west*.")
    print("What will you do?\n")
    
    while True:
        choice = input("░ ").lower().strip()

        if choice in('w', 'west', 'go west'):
            if room_13_open:
                room_13()
                break
            else: 
                print("\nThe door is locked. There's moaning coming from inside.\n")
        elif choice in ('s', 'south', 'go south'):
            room_14()
            break
        elif choice in ('look', 'examine') or choice.startswith("examine ") or choice.startswith("look "):
            if choice in ('look', 'examine'):
                print("\nRows upon rows of flashing indicator lights stretch into the darkness, illuminating towering black server racks that dominate the space.")
                print("Cables, thick as pythons, snake across the metallic floor and up the walls.\n")
            else:
                target = choice.split(" ", 1)[1]
                examine_item(target, room_items)
        elif choice.startswith("drop "):
            item = choice[5:]
            drop_item(item, room_items, inventory)        
        elif choice in ("inventory", "i"):
            show_inventory()
        elif choice == "help":
            help_menu()
        elif choice in ("quit", "exit"):
            handle_quit()
        else:
            print("\nI don't understand.\n")    

# Room 13 / WC
def room_13():
    global room_13_open
    time.sleep(3)
    print(r''' 
                 _____
                /      \
               (____/\  )
               |___  U?(____
               _\L.   |      \    ___
             / /"""\ /.-'     |  |\  |
            ( /  _/u     |    \__|_) |
            \|  \\      /   / \_(___ __)
             |   \\    /   /  |  |    |
             |    )  _/   /   )  |    |
              \__/.-'    /___(   |    |    
          _/  __________/     \  |    |
         //  /  (              ) |    |
        ( \__|___\    \______ /__|____|
         \    (___\   |______)_/            ░ splosh.
          \   |\   \  \     /
           \  | \__ )  )___/
            \  \  )/  /__(       
        ___ |  /_//___|   \_________
           _/  ( /         \
          `----'(___________)
        ''')   
    print("Whoa, Frank, you were quick! I didn't even bother locking up.")
    print("Now get the fuck out and let me meditate!")
    room_13_open = False
    time.sleep(3)
    room_12()
    return

# Room 14 / PC
def room_14():
    room_items = []
    print("\nYou climb the stairs and enter a small room made of gray metal and concrete.")
    print("In the center of the room is a desk. There's an old computer on it.")
    print("You can go *south* back downstairs.")
    print("What will you do?\n")

    while True:
        choice = input("░ ").lower().strip()

        if choice in ("s", "south", "go south"):
            room_12()
            break
        elif choice in ("look", "examine") or choice.startswith("examine ") or choice.startswith("look "):
            if choice in ("look", "examine"):
                print("\nThe room is small and dim, smelling faintly of burnt coffee.")
                print("A single gray metal desk holds a silently humming desktop computer.\n")
            else:
                target = choice.split(" ", 1)[1]
                examine_item(target, room_items)
        elif choice in ("use computer", "use pc", "use usb", "use usb stick", "insert usb", "plug usb"):
            if "usb stick" in inventory:
                print("\nYou take out the small USB stick and plug it into the office computer's USB port.")
                time.sleep(1)
                print("The screen flickers, then a login prompt appears asking for username.")
                username = input("Username: ").strip()
                if username.lower() == "frank":
                    print_slow("\nＡＣＣＥＳＳ ＧＲＡＮＴＥＤ．\n")
                    time.sleep(2)
                    print_slow("Username: ＦＲＡＮＫ\n")
                    print_slow("Simulation: ＫＮＩＧＨＴ＇Ｓ ＱＵＥＳＴ ４．２．１． － ＡＷＡＩＴＩＮＧ ＤＥＬＥＴＩＯＮ ＰＲＯＴＯＣＯＬ．．．\n")
                    time.sleep(2)
                    print_slow("ＩＮＩＴＩＡＴＩＮ ＳＥＱＵＥＮＣＥ ＳＴＡＲＴＥＤ．．．\n")
                    time.sleep(2)
                    print_slow("．．．ＤＥＬＥＴＩＯＮ ＣＯＭＰＬＥＴＥＤ． ＳＨＵＴＤＯＷＮ ＩＮ Ｔ－３．．．２．．．１．．．\n")
                    time.sleep(5)
                    exit()
                else:
                    print("\nAccess denied. That username is incorrect.\n")
            else:
                print("\nYou don't have a USB stick to use here.\n")
        elif choice.startswith("drop "):
            item = choice[5:]
            drop_item(item, room_items, inventory)
        elif choice in ("inventory", "i"):
            show_inventory()
        elif choice == "help":
            help_menu()
        elif choice in ("quit", "exit"):
            handle_quit()
        else:
            print("\nI don't understand.\n")

# Start
time.sleep(2)
room_1()