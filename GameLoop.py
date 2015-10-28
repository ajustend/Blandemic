import random
import sys

import deckDB
import playerDB
import roleDB



## Game Setup BEGIN

## Information to get: # of Players, Difficulty (Beginner, Normal, Hard)


while True:
    num_players = int(input("\nHow many players? 2-4:"))
    if num_players >= 2 and num_players <= 4:
        print("\nOk, %s players." % num_players)
        break
    else:
        print("\nERROR - Choose a number between 2 and 4, please.")

## Shuffle RoleCard, deal and assign 1 Role to each Player.

rand_role_card = roleDB.role_card_list[random.randrange(len(roleDB.role_card_list))]

input("\n\nPress ENTER to be assigned a Role Card")

roleDB.assign_role_card(num_players)


## Shuffle Playerdeck, deal StartingHand to each Player based on # of Players.

input("\n\nPress ENTER to shuffle Player Deck and Deal Starting Hands.")

p_deck = deckDB.Deck()

# print("Cards in Player deck before shuffle: %s" % p_deck.card_list)
random.shuffle(p_deck.card_list)
# print("Cards in Player deck after shuffling: %s" % p_deck.card_list)
# print("%s cards in Player Deck" % len(p_deck.card_list))


## Deals starting hand to players based on number of players


def deal_starting_hand(num):
    if num == 2:
        ##Creates a player's starting hand for 2
        print("\nPlayer 1's hand:")
        for i in range(4):
            playerDB.player_1_hand.append(p_deck.card_list[0])
            print("  ", playerDB.player_1_hand[i][1])
            p_deck.card_list.remove(p_deck.card_list[0])
        print("\nPlayer 2's hand:")
        for i in range(4):
            playerDB.player_2_hand.append(p_deck.card_list[0])
            print("  ", playerDB.player_2_hand[i][1])
            p_deck.card_list.remove(p_deck.card_list[0])
    elif num == 3:
        ##Creates a player's starting hand for 3
        print("\nPlayer 1's hand:")
        for i in range(3):
            playerDB.player_1_hand.append(p_deck.card_list[0])
            print("  ", playerDB.player_1_hand[i][1])
            p_deck.card_list.remove(p_deck.card_list[0])
        print("\nPlayer 2's hand:")
        for i in range(3):
            playerDB.player_2_hand.append(p_deck.card_list[0])
            print("  ", playerDB.player_2_hand[i][1])
            p_deck.card_list.remove(p_deck.card_list[0])
        print("\nPlayer 3's hand:")
        for i in range(3):
            playerDB.player_3_hand.append(p_deck.card_list[0])
            print("  ", playerDB.player_3_hand[i][1])
            p_deck.card_list.remove(p_deck.card_list[0])
    elif num == 4:
        ##Creates a player's starting hand for 4
        print("\nPlayer 1's hand:")
        for i in range(2):
            playerDB.player_1_hand.append(p_deck.card_list[0])
            print("  ", playerDB.player_1_hand[i][1])
            p_deck.card_list.remove(p_deck.card_list[0])
        print("\nPlayer 2's hand:")
        for i in range(2):
            playerDB.player_2_hand.append(p_deck.card_list[0])
            print("  ", playerDB.player_2_hand[i][1])
            p_deck.card_list.remove(p_deck.card_list[0])
        print("\nPlayer 3's hand:")
        for i in range(2):
            playerDB.player_3_hand.append(p_deck.card_list[0])
            print("  ", playerDB.player_3_hand[i][1])
            p_deck.card_list.remove(p_deck.card_list[0])
        print("\nPlayer 3's hand:")
        for i in range(2):
            playerDB.player_4_hand.append(p_deck.card_list[0])
            print("  ", playerDB.player_4_hand[i][1])
            p_deck.card_list.remove(p_deck.card_list[0])


deal_starting_hand(num_players)

# print("\nCards in Player deck after dealing starting hands: %s" % p_deck.card_list)

## Cut remaining PlayerDeck into 1 pile for each Epidemic Card added in (based on
## difficulty level) and add an Epidemic card randomly inside each one.


while True:
    difficulty_level = int(input("\n\nChoose difficulty level, \n1)beginner "
                                 "\n2)regular \n3)hard. \n\n1-3:"))
    if difficulty_level >= 1 and difficulty_level <= 3:
        break
    else:
        print("ERROR - Choose a number between 1 and 3, please.")


def add_epidemic_cards(difficulty):
    if difficulty == 1:
        epidemic_cards = 4
        small_deck_size = len(p_deck.card_list)//epidemic_cards
        for i in range(epidemic_cards):
            p_deck.card_list.insert(random.randrange(small_deck_size*i, small_deck_size*(i+1), 1), "EPIDEMIC!")
            #print("%s cards in currently shuffled Player Deck" % len(p_deck.card_list))
    elif difficulty == 2:
        epidemic_cards = 5
        small_deck_size = len(p_deck.card_list)//epidemic_cards
        for i in range(epidemic_cards):
            p_deck.card_list.insert(random.randrange(small_deck_size*i, small_deck_size*(i+1), 1), "EPIDEMIC!")
            #print("%s cards in currently shuffled Player Deck" % len(p_deck.card_list))
    elif difficulty == 3:
        epidemic_cards = 6
        small_deck_size = len(p_deck.card_list)//epidemic_cards
        for i in range(epidemic_cards):
            p_deck.card_list.insert(random.randrange(small_deck_size*i, small_deck_size*(i+1), 1), "EPIDEMIC!")
            #print("%s cards in currently shuffled Player Deck" % len(p_deck.card_list))

    else:
        pass


add_epidemic_cards(difficulty_level)

# print("\nPlayer Deck with Epidemics added: {0}".format(p_deck.card_list))

input("\n"
      "** Player Deck Complete **\n"
      "Press ENTER to build Infection Deck.")

## Shuffle Infection Deck

i_deck = deckDB.Deck()
# print("\nalphabetical Infection Deck: {0}".format(i_deck.card_list))
random.shuffle(i_deck.card_list)
# print("\nshuffled Infection Deck: {0}".format(i_deck.card_list))

input("\n"
      "** Infection Deck Complete **\n"
      "Press ENTER to Infect Starting Cities.\n")

# Instantiate the cities with CityDB(), these city 'tokens' will be used to
# track infections, research center flags, connected cities (for outbreaks
# and movement), color, and name.

# The methods in the CityDB class allow you to infect cities incrementally,
# set an infection level, and trigger an outbreak (infects every connected city
# with one infection counter)

city_list = {"algiers": {"name": "Algiers, Algeria",
           "color": "Black",
           "connected_cities": ['madrid', 'paris', 'istanbul', 'cairo'],
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"atlanta": {"name": "Atlanta, USA",
           "color": "Blue",
           "connected_cities": ['chicago', 'washington', 'miami'],
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 1},
"baghdad": {"name": "Baghdad, Iraq",
           "color": "Black",
           "connected_cities": ['tehran', 'karachi', 'riyadh',
                                'cairo', 'istanbul'],
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"bangkok": {"name": "Bangkok, Thailand",
           "color": "Red",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"beijing": {"name": "Beijing, China",
           "color": "Red",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"bogota": {"name": "Bogota, Colombia",
            "color": "Yellow",
            "connected_cities": "",
            "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
            "research_station": 0},
"buenos_aires": {"name": "Buenos Aires, Argentina",
           "color": "Yellow",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"cairo": {"name": "Cairo, Egypt",
           "color": "Black",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"chennai": {"name": "Chennai, India",
           "color": "Black",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"chicago": {"name": "Chicago, USA",
           "color": "Blue",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"delhi": {"name": "Delhi, India",
           "color": "Black",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"essen": {"name": "Essen, Germany",
           "color": "Blue",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"ho_chi_minh_city": {"name": "Ho Chi Minh City, Vietnam",
           "color": "Red",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"hong_kong": {"name": "Hong Kong",
           "color": "Red",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"istanbul": {"name": "Istanbul, Turkey",
           "color": "Black",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"jakarta": {"name": "Jakarta, Indonesia",
           "color": "Red",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"johannesburg": {"name": "Johannesburg, South Africa",
           "color": "Yellow",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"karachi": {"name": "Karachi, Pakistan",
           "color": "Black",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"khartoum": {"name": "Khartoum, Sudan",
           "color": "Yellow",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"kinshasa": {"name": "Kinshasa, Congo",
           "color": "Yellow",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"kolkata": {"name": "Kolkata, India",
           "color": "Black",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"lagos": {"name": "Lagos, Nigeria",
           "color": "Yellow",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"lima": {"name": "Lima, Peru",
           "color": "Yellow",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"london": {"name": "London, England",
           "color": "Blue",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"los_angeles": {"name": "Los Angeles, USA",
           "color": "Yellow",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"madrid": {"name": "Madrid, Spain",
           "color": "Blue",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"manila": {"name": "Manila, Phillipines",
           "color": "Red",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"miami": {"name": "Miami, USA",
           "color": "Yellow",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"milan": {"name": "Milan, Italy",
           "color": "Blue",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"mexico_city": {"name": "Mexico City, Mexico",
           "color": "Yellow",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"montreal": {"name": "Montreal, Canada",
           "color": "Blue",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"moscow": {"name": "Moscow, Russia",
           "color": "Black",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"mumbai": {"name": "Mumbai, India",
           "color": "Black",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"new_york": {"name": "New York, USA",
           "color": "Blue",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"osaka": {"name": "Osaka, Japan",
           "color": "Red",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"paris": {"name": "Paris, France",
           "color": "Blue",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"riyadh": {"name": "Riyadh, Saudi Arabia",
           "color": "Black",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"santiago": {"name": "Santiago, Chile",
           "color": "Yellow",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"san_francisco": {"name": "San Francisco, USA",
           "color": "Blue",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"sao_paulo": {"name": "Sao Paulo, Brazil",
           "color": "Yellow",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"seoul": {"name": "Seoul, South Korea",
           "color": "Red",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"shanghai": {"name": "Shanghai, China",
           "color": "Red",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"st_petersburg": {"name": "St. Petersburg, Russia",
           "color": "Blue",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"sydney": {"name": "Sydney, Australia",
           "color": "Red",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"taipei": {"name": "Taipei, Taiwan",
           "color": "Red",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"tehran": {"name": "Tehran, Iran",
           "color": "Black",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"tokyo": {"name": "Tokyo, Japan",
           "color": "Red",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},
"washington": {"name": "Washington, USA",
           "color": "Blue",
           "connected_cities": "",
           "city_infection_counter": {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0},
           "research_station": 0},}

# print("\n{0} cards in shuffled Infection Deck".format(len(i_deck.deck)))

# Create Disease Bank Dict to keep track of remaining disease cubes.
# Create function to Infect Cities.


disease_bank = {'yellow': 24, 'red': 24, 'blue': 24, 'black': 24}
discovered_cure = {'yellow': 0, 'red': 0, 'blue': 0, 'black': 0}


def infect_city(amount_cubes= 1, amount_cities= 1, pop_point= -1):
    for i in range(amount_cities):
        # print("** START Infection Process **")
        active_card = i_deck.card_list.pop(pop_point)
        # print("Active Card:", active_card)
        city_list[active_card[1]]['city_infection_counter'][active_card[2]] += amount_cubes
        # print("{0} infected with {1} {2} cubes.".format(active_card[0], amount_cubes, active_card[2]))
        disease_bank[active_card[2]] -= amount_cubes
        # print("{0} Disease Cube total: {1}".format(active_card[2], disease_bank[active_card[2]]))
        i_deck.discard.append(active_card)
        # print("Discard Pile:", i_deck.discard)
        # print("** END Infection Process **")


# Deal top 3 Infection Cards face up, Add 3 Disease Cubes to each of the cities,
# Remove those Disease Cubes from bank, Send Infection Cards to Discard pile.



print("\nInfected with 3 Disease Cubes:")
print("  ",format(i_deck.card_list[-1][0]))
print("  ",format(i_deck.card_list[-2][0]))
print("  ",format(i_deck.card_list[-3][0]))

infect_city(3, 3)

# Deal next 3 Infection Cards face up, Add 2 DiseaseCube to each of the cities,
# send those cards to discard pile.

print("\nInfected with 2 Disease Cubes:")
print("  ",format(i_deck.card_list[-1][0]))
print("  ",format(i_deck.card_list[-2][0]))
print("  ",format(i_deck.card_list[-3][0]))

infect_city(2, 3)

# Deal next 3 Infection Cards face up, Add 1 DiseaseCube to each of the cities,
# send those cards to discard pile.

print("\nInfected with 1 Disease Cube:")
print("  ",format(i_deck.card_list[-1][0]))
print("  ",format(i_deck.card_list[-2][0]))
print("  ",format(i_deck.card_list[-3][0]))

infect_city(1, 3)

print("\n** City Infection Complete **")

# print("\n{0} cards in shuffled Infection Deck".format(len(i_deck.deck)))

## Set OutbreakMarker to 0


outbreak_counter = 0


def bump_outbreak():
    outbreak_counter += 1

## InfectionRate to 2 (0 position)

infection_level_list = [2, 2, 2, 3, 3, 4, 4]

infection_level_counter = 0


def bump_infection_level():
    infection_level_counter += 1


def get_infection_level():
    return infection_level_list[infection_level_counter]

## Game Setup COMPLETE



##Begin Play

## Main Game Loop

## Set Game Over conditions:

while True:
    if len(p_deck.card_list) <= 0:
        print("GAME OVER")
        break
    elif outbreak_counter == 8:
        print("GAME OVER")
        break
    elif disease_bank['yellow'] == 0 or disease_bank['red'] == 0 or \
                    disease_bank['blue'] == 0 or disease_bank['black'] == 0:
        print("GAME OVER")
        break
    else:
        pass


##Player Turn Loop




#print("%s has %s Actions left." % (playerName_01, actionsRemaining) )

#def playerTurn_actionPhase():
#    print("1. Move")
#    print("2. Treat Disease")
#    print("3. Build Research Station")
#    print("4. Share Knowledge")
#    playerAction_01 = int(input())
#    if playerAction_01 == 1:

#    return playerAction_01

# def actionLoop():
#     for action in range (1,5):
#         print("Action", action)
#         step1 = int(input("1-5?"))
#         if step1 == 1:
#             print("Move. Where?")
#         elif step1 == 2:
#             print("Color disease treated. x remain.")
#         elif step1 == 3:
#             print("Research Station built.")
#         elif step1 == 4:
#             print("Knowledge shared.")
#         else:
#             turnEndConfirm = input("Are you SURE you want to END turn? y/n?")
#             if turnEndConfirm == "y":
#                 print("Turn ended.")
#                 break
#             else:
#                 print("exit cancelled")


sys.exit()