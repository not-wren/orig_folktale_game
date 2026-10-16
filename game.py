from telnetlib import SUPPRESS_LOCAL_ECHO
room = "starting"
treasure = 0
game_running = True


while game_running:
    if room == "starting":
        print("After partying all night for Halloween, you wake up and find yourself in a dungeon-looking room.")
        print("You remember the number 7 is important. You see a spider on the wall, and a door to enter the room with a Danger sign.")
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
        if ritual == "zephyr" and treasure >= 1:
            print("You get teleported back to the party with gold. You invest it in a research facility to study interdimensional spiders.")
            print("A few years after the party, now people can teleport because of your researc.")
            print("Ending 2/2: Spider Warping")
            game_running = False
        elif ritual == "zephyr":
            print ("You are teleported back to the party. You escaped!")
            print ("But you remember you were actually a researcher who needed money from the realm you were just in.")
            print ("A few years later, a radiactive spider bites you.")
            print ("Ending 1/2: Spider-man??")
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
    
    elif response == "2":
        print("She says the code is zephyr.")

    elif room == "padlock":
        print("You look at the padlocked door. It can only take a single digit number. You try recalling an important number.")
        response == input("Single digit number:")
        if response == "7":
            print("You walk into the room and spot gold coins. You take them with you.")
            treasure += 1
        else:
            print("You suddenly pass out from being too tired.")
            room = "starting"
