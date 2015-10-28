__author__ = 'JMullens'

import random, os, math

import deckDB, cityDB, playerDB

role_card_list = ["Contingency Planner", "Operations Expert", "Dispatcher",
                "Quarantine Specialist", "Researcher", "Scientist", "Medic"]

def assign_role_card(num):
    for i in range(num):
        playerDB.playerList[i].update({"role":(role_card_list[random.randrange(len(role_card_list))])})
        role_card_list.remove(playerDB.playerList[i]["role"])
        print("\nPlayer %s is the %s" % (i+1, playerDB.playerList[i]["role"]))

    ##to double check the actual assignment in each list
    #print("player_1 is", player_1)
    #print("player_2 is", player_2)
    #print("player_3 is", player_3)
    #print("player_4 is", player_4)