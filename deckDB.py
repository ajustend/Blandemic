__author__ = 'JMullens'

import random


class Deck(object):
    def __init__(self):
        algiers = ["Algiers", "algiers", "black"]
        atlanta = ["Atlanta", "atlanta", "blue"]
        baghdad = ["Baghdad", "baghdad", "black"]
        bangkok = ["Bangkok", "bangkok", "red"]
        beijing = ["Beijing", "beijing", "red"]
        bogota = ["Bogota", "bogota", "yellow"]
        buenos_aires = ["Buenos Aires", "buenos_aires", "yellow"]
        cairo = ["Cairo", "cairo", "black"]
        chennai = ["Chennai", "chennai", "black"]
        chicago = ["Chicago", "chicago", "blue"]
        delhi = ["Delhi", "delhi", "black"]
        essen = ["Essen", "essen", "blue"]
        ho_chi_minh_city = ["Ho Chi Minh City", "ho_chi_minh_city", "red"]
        hong_kong = ["Hong Kong", "hong_kong", "red"]
        istanbul = ["Istanbul", "istanbul", "black"]
        jakarta = ["Jakarta", "jakarta", "red"]
        johannesburg = ["Johannesburg", "johannesburg", "yellow"]
        karachi = ["Karachi", "karachi", "black"]
        khartoum = ["Khartoum", "khartoum", "yellow"]
        kinshasa = ["Kinshasa", "kinshasa", "yellow"]
        kolkata = ["Kolkata", "kolkata", "black"]
        lagos = ["Lagos", "lagos", "yellow"]
        lima = ["Lima", "lima", "yellow"]
        london = ["London", "london", "blue"]
        los_angeles = ["Los Angeles", "los_angeles", "yellow"]
        madrid = ["Madrid", "madrid", "blue"]
        manila = ["Manila", "manila", "red"]
        mexico_city = ["Mexico City", "mexico_city", "yellow"]
        miami = ["Miami", "miami", "yellow"]
        milan = ["Milan", "milan", "blue"]
        montreal = ["Montreal", "montreal", "blue"]
        moscow = ["Moscow", "moscow", "black"]
        mumbai = ["Mumbai", "mumbai", "black"]
        new_york = ["New York", "new_york", "blue", ]
        osaka = ["Osaka", "osaka", "red"]
        paris = ["Paris", "paris", "blue"]
        riyadh = ["Riyadh", "riyadh", "black"]
        san_francisco = ["San Francisco", "san_francisco", "blue"]
        sao_paulo = ["Sao Paulo", "sao_paulo", "yellow"]
        santiago = ["Santiago", "santiago", "yellow"]
        seoul = ["Seoul", "seoul", "red"]
        shanghai = ["Shanghai", "shanghai", "red"]
        st_petersburg = ["St. Petersburg", "st_petersburg", "blue"]
        sydney = ["Sydney", "sydney", "red"]
        taipei = ["Taipei", "taipei", "red"]
        tehran = ["Tehran", "tehran", "black"]
        tokyo = ["Tokyo", "tokyo", "red"]
        washington = ["Washington", "washington", "blue"]

        self.card_list = [algiers, atlanta, baghdad, bangkok, beijing, bogota,
                      buenos_aires, cairo, chennai, chicago, delhi, essen,
                      ho_chi_minh_city, hong_kong, istanbul, jakarta,
                      johannesburg, karachi, khartoum, kinshasa, kolkata,
                      lagos, lima, london, los_angeles, madrid, manila,
                      mexico_city, miami, milan, montreal, moscow, mumbai,
                      new_york, osaka, paris, riyadh, san_francisco, sao_paulo,
                      santiago, seoul, shanghai, st_petersburg, sydney, taipei,
                      tehran, tokyo, washington]

        self.deck = []

        self.discard = []

    def shuffle(self):
        self.shuffled = random.sample(self.card_list, len(self.card_list))
        return self.shuffled

    def shuffle_discard(self):
        self.discard = random.sample(self.discard, len(self.discard))
        return self.discard

    def add_discard_to_deck(self, target):
        target.insert(0, self.discard[0:80])
        self.discard.clear()

    def shuffle_with_discard(self):
        combined = self.extend(self.discard)
        self.shuffled = random.sample(combined, len(combined))
        return self.shuffled

    def draw_card(self):
        global active_card
        active_card = self.pop()
        print("%s is drawn." % active_card)

    def draw_to_hand(self, active_player):
        global active_card
        active_card = self.pop()
        active_player.hand.append(active_card)
        print("{0} has been sent to {1}'s hand.".format(active_card, active_player))

    def draw_to_discard(self):
        global active_card
        active_card = self.pop()
        self.discard.append(active_card)
        print("{0} has been sent to the discard pile.".format(active_card))


# p_deck = Deck()
# i_deck = Deck()
# print("P-Deck:", p_deck.card_list)
# print("I-Deck:", i_deck.card_list)
# random.shuffle(p_deck.card_list)
# random.shuffle(i_deck.card_list)
# print("P-Deck:", p_deck.card_list)
# print("I-Deck:", i_deck.card_list)


# ## Assign a deck object
# pd = Deck()
# id = Deck()
# ## Print the deck contents
# print(pd.card_list)
# print(id.card_list)
# ## Shuffle the deck
# pd_shuffled = pd.shuffle()
# id_shuffled = id.shuffle()
# ## Print the shuffled deck
# print(pd_shuffled)
# print(id_shuffled)
# ## Draw a card
# drawn_card = pd_shuffled.pop(0)
# print(drawn_card)
# ## Print the shuffled deck
# print(pd_shuffled)


# ## Make a deck, shuffle it, top card to discard * 3,
# ##     shuffle discard, add discard to top of deck.
# i_deck = Deck()
# print("Deck:",i_deck.card_list)
# random.shuffle(i_deck.card_list)
# print("Shuffled Deck:", i_deck.card_list)
# for i in range(3):
#     active_card = i_deck.card_list.pop()
#     print("Active Card:", active_card)
#     i_deck.discard.append(active_card)
#     print("Discard Pile:", i_deck.discard)
#     print("Shuffled Deck:", i_deck.card_list)
# random.shuffle(i_deck.discard)
# print("Shuffled Discard Pile:", i_deck.discard)
# i_deck.card_list.append(i_deck.discard)
# print("Discard Added to Deck:", i_deck.card_list)










