#list of rooms stored as tuples
#player moves, monster stays, room stays
#player must find room
#add grid with breadcrumbs

#IMPORTANT note__
#find x, or east west coordinates (a, b), for player by using player_room[0]
#find y, or north south coordinates (1, 2), for player by using player_room[1]

import random

#Establish rooms
rooms = (['a', 1], ['b', 1], ['a', 2], ['b', 2])
x_index_list = ['a', 'b']
y_index_list = [1, 2]

#Generate rooms
monster_room = random.choice(rooms)
door_room = random.choice(rooms)

#Set up player
player_room = random.choice(rooms)
player_x = player_room[0]
player_y = int(player_room[1])

def player_movement():
    move = input("Where would you like to move? ")
    if move == "UP":
        #take player_room y coordinate
        #move it up in the y index, if possible movement exists
        try:
            global player_y
            player_y += 1
            y_index_list.index(player_y)
        except ValueError:
            print("Not a valid movement!")
            player_y -= 1
    elif move == "DOWN":
        try:
            global player_y
            player_y -= 1
            y_index_list.index(player_y)
        except ValueError:
            print("Not a valid movement!")
            player_y += 1
    print(player_y)

player_movement()

#While True:
#    if player_room == monster_room:
#        print("The monster got you! \n Please play again!")
#        break
#    elif player_locaiton == door_room:
#        print("You found the exit! \n Please play again!)
#        break
#    else:
#        player_movement()
