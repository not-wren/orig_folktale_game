from telnetlib import SUPPRESS_LOCAL_ECHO
room = "starting"
game_running = True

while game_running:
    if room == "starting":
        print("After partying all night for Halloween, you wake up and find yourself in a dungeon-looking room.")
        print("You see a spider on the wall, and a door to enter the room with a Danger sign. You remember 7 is important.")
        print("To talk to the spider, press 1. To enter the Danger room, press 2.")

        answer = input("1-2: ")

        if answer == "1":
            room = "spider"
        elif answer == "2":
            room = "danger"
        else:
            print("hint: press one or two!")

    elif room == "spider":
        print("The spider looks at you, and says it needs you to say the ritual phrase and then it can take you back to the real world.")
        ritual = input("Ritual phrase: ").lower()
        if ritual == "zephyr":
            print ("You are teleported back to the party. You escaped!")
            game_running = False
        else:
            print("The spider shakes its head, disappointed.")
        room = "starting"

    elif room == "danger":
        print("The danger room is actually pretty cozy looking, and a girl wearing a moth costume is standing there.")
        print("She starts talking to you.")
        print("Do you prefer spiders or moths?")
        print("Choose your response:")
        print("1. moths")
        print("2. spiders")

    response = input("1-2")
    if response == "1":
        print("She smiles, and moves to the other corner of the room, revealing a padlocked door.")
        room = "padlock"
        if room = "padlock":
    elif response == "2":
        print("She says the code is zephyr.")