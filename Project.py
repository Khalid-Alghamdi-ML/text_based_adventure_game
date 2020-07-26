import time
import random

gun = False


# function to create delays between messages
def msg(massege):
    time.sleep(0.5)
    print(massege)
    time.sleep(0.5)


# function for randomness
def rand():
    return random.choice(["zombie", "werewolf", "vampire", "kikimora"])


# function for player option
def option(choice):
    choice = input("\nPlease choose 1 or 2: ")
    return choice


# strating the game
def play():
    msg("You are at the first room in a an abandoned house\n")
    msg("there two doors in front of you\n")
    msg("do you want to enter?\n1.Black door\n2.White door")
    while True:
        player_choice = option("choice")
        if player_choice == "1":
            black()
            break
        elif player_choice == "2":
            white()
            break


# middle of the game or the main HUB
def main_room():
    msg("\nYou are back to the first room\n")
    msg("do you want to enter?\n1.Black door\n2.White door")
    while True:
        player_choice = option("choice")
        # indicating that first option already choosed and item was taken
        if player_choice == "1":
            msg("\nYou have been there, there is nothing else in the room\n")
            main_room()
            break
        elif player_choice == "2":
            white()
            break


# first option to have the item
def black():
    msg("\nAfter opening the black door\n")
    msg("you found a gun!\n")
    msg("you grab it and go back to the first room")
    global gun
    gun = True
    main_room()


def white():
    msg("\nWhen you open the door you noticed a shiny object",
        "at the right corner of the room\n")
    msg("you aproach the object and suddenly a " + rand() + " jump on you\n")
    msg("do you want to:\n1.Fight\n2.Run\n")
    # checing for the item
    if gun is False:
        while True:
            player_choice = option("choice")
            if player_choice == "1":
                msg("\nYou have nothing to use for protecting yourself\n")
                msg("You died")
                again()
                break
            elif player_choice == "2":
                print("\nYou run to the first room",
                      "and close the door behind you\n")
                main_room()
                break
    elif gun is True:
        while True:
            player_choice = option("choice")
            if player_choice == "1":
                msg("\nYou use the gun to shoot the "
                    + rand() + " and manage to kill it")
                msg("You win the game!!!")
                again()
                break
            elif player_choice == "2":
                print("\nYou run to the first room",
                      "and close the dore behind you\n")
                main_room()
                break


# function for restating the game
def again():
    msg("\nWould you like to restart the game?\n")
    msg("1.Restart\n2.Shutdown")
    while True:
        player_choice = option("choice")
        if player_choice == "1":
            msg("\nReastarting the game...\n")
            # removing the item for restarting the game
            global gun
            gun = False
            play()
            break
        elif player_choice == "2":
            msg("\nThank you for playing")
            break


# executing last to avoid errors
play()
