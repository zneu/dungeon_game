#list of rooms stored as tuples
#player moves, monster stays, room stays
#player must find door room
#add grid with breadcrumbs

#IMPORTANT note__
#find x, or east west coordinates (a, b), for player by using player_room[0]
#find y, or north south coordinates (1, 2), for player by using player_room[1]

import random

#Establish rooms
rooms = (['a', 1], ['b', 1], ['c', 1], ['d', 1],
['a', 2], ['b', 2], ['c', 2], ['d', 2],
['a', 3], ['b', 3], ['c', 3], ['d', 3],
['a', 4], ['b', 4], ['c', 4], ['d', 4])

x_index_list = ['a', 'b', 'c', 'd']
y_index_list = [1, 2, 3, 4]

#Generate rooms
monster_room = random.choice(rooms)
door_room = random.choice(rooms)

#Set up player
player_room = random.choice(rooms)

#if player_room == monster_room or door_room:
#    player_room = random.choice(rooms)
#else:
#    print("player is in room {}".format(player_room))

player_x = player_room[0]
player_y = int(player_room[1])

def show_help():
    print("\nType 'up', 'down', 'left', or 'right' to move your character. "
    "Type 'quit' to exit the application and 'help' to show this help text.")

def player_movement():
    move = input("Where would you like to move? ").lower()
    global player_y
    global player_x
    if move == "up":
        #take player_room y coordinate
        #move it up in the y index, if possible movement exists
        try:
            player_y += 1
            y_index_list.index(player_y)
            player_room[1] += 1
        except ValueError:
            print("\nNot a valid movement!")
            player_y -= 1

    elif move == "down":
        try:
            player_y -= 1
            y_index_list.index(player_y)
            player_room[1] -= 1
        except ValueError:
            print("\nNot a valid movement!")
            player_y += 1

    elif move == "right":
        try:
            player_x = x_index_list[(x_index_list.index(player_x)) + 1]
            player_room[0] = player_x
        except IndexError:
            print("\nThat's not a  valid move!")

    elif move == "left":
        if (x_index_list.index(player_x) - 1) >= 0:
            player_x = x_index_list[(x_index_list.index(player_x)) - 1]
            player_room[0] = player_x
        else:
            print("\nThat's not a valid move!")

    elif move == "quit":
        print("\nThank you for playing!")
        quit()

    elif move == "help":
        show_help()

    else:
        print("\nhat's not a command!")

show_help()

while True:
    print("\nplayer is in room {}".format(player_room))
    if player_room == monster_room:
        print("The monster got you! \nPlease play again!")
        break
    elif player_room == door_room:
        print("You found the exit! \nPlease play again!")
        break
    else:
        player_movement()
