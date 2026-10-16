from telnetlib import SUPPRESS_LOCAL_ECHO
room = "starting"
correct = 0
game_running = True

while game_running:
    if room == "starting":
        print("After partying all night for Halloween, you wake up and find yourself in a dungeon-looking room.")
        print("You see a spider on the wall, and a door to enter the room with a Danger sign")
        print("To talk to the spider, press 1. To enter the Danger room, press 2.")

        answer = input("1-2: ")

        if answer == "1":
            room = "spider"
        elif answer == "2":
            room = "danger"
        else:
            print("hint: press one or two!")

    elif room == "spider"
        print("The spider looks at you, and says it needs you to say the ritual phrase,")
        print("so it can take you back to the real world.")
        ritual = input
        if 