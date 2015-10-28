__author__ = 'JMullens'

import random, os, math

import deckDB, cityDB, roleDB

class Player(object):
    def __init__(self, name="name", role="role", startX=0, startY=0):
        self.name = name
        self.role = role
        self.hand = []
        self.actions_counter = 0
        self.xy = [startX, startY]

    def get_name(self):
        return self.name

    def set_name(self, x):
        self.name = x

    def get_role(self):
        return self.role

    def set_role(self, x):
        self.role = x

    def get_position(self):
        return self.xy

    def set_position(self, x, y):
        self.xy = [x, y]

    def get_hand(self):
        return self.hand

    # def __str__(self):
    #     return self.name + " " + self.role + " " + \
    #            "x=" + str(self.x) + " " + "y=" + str(self.y)

# p = Player()
# p.set_name("Frank")
# print(p.get_name())
# p.set_position(3,4)
# print(p.get_position())



## Example: player1 = Player("Julio", "Medic", 8, 10)

class Hand(Player):
    def __init__(self):
        self.hand = []

    def __str__(self):
        return print(player)

# player1 = Player()
#
# print(player1.get_hand)

# print(hand1)


player_1 = {"name" : "",
            "role" : "",
            "hand" : "player_1_hand",
            "actions_counter" : "4",
            "position" : ""}
player_1_hand = []
player_2 = {"name" : "",
            "role" : "",
            "hand" : "player_1_hand",
            "actions_counter" : "4",
            "position" : ""}
player_2_hand = []
player_3 = {"name" : "",
            "role" : "",
            "hand" : "player_1_hand",
            "actions_counter" : "4",
            "position" : ""}
player_3_hand = []
player_4 = {"name" : "",
            "role" : "",
            "hand" : "player_1_hand",
            "actions_counter" : "4",
            "position" : ""}
player_4_hand = []

##Creating a list of the Dicts so they can be called using variables

playerList = [player_1, player_2, player_3, player_4]
