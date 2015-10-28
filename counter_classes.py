__author__ = 'JMullens'


class Counter(object):
    def __init__(self, starting_point=0):
        self.value = starting_point

    def get(self):
        return self.value

    def set(self, new_value):
        self.value = new_value

    def add(self, amount=1):
        self.value += amount

    def subtract(self, amount=1):
        self.value -= amount

    def sub(self, amount=1):
        self.value -= amount

# wheel = Counter(5)
# print(wheel.get())
# wheel.add()
# wheel.add()
# print(wheel.get())
# wheel.sub()
# print(wheel.get())
# print(wheel.set(2))
# wheel.set(2)
# print(wheel.get())


class PlayerActions(Counter):
    def __init__(self, starting_point=4):
        self.value = starting_point
    # def __str__(self):
    #     return self.value

# pac = PlayerActions()
# print(pac)
# print(pac.value)
# pac.subtract()
# print(pac.value)


class CuredDiseases(Counter):

    color_lookup = {"black":0, "blue":1, "red":2,
                     "yellow":3}

    black = color_lookup["black"]
    blue = color_lookup["blue"]
    red = color_lookup["red"]
    yellow = color_lookup["yellow"]

    def __init__(self):
        self.blackDisease = [0, 0] # [cured?, eradicated?]
        self.blueDisease = [0, 0]
        self.redDisease = [0, 0]
        self.yellowDisease = [0, 0]
        self.db = [self.blackDisease, self.blueDisease,
                   self.redDisease, self.yellowDisease]


    def cure(self, color_location):
        self.db[color_location][0] = 1

    def eradicate(self, color_location):
        self.db[color_location][1] = 1

    def checkCure(self):
        for color in range(4):
            if cdc.db[color][0] == 1 and cdc.db[color][1] == 1:
                print("%s is cured & eradicated." % color)
            elif cdc.db[color][0] == 1 and cdc.db[color][1] == 0:
                print("%s is cured." % color)
            elif cdc.db[color][0] == 0:
                print("%s has NOT been cured." % color)
            else:
                print("assert")

# cdc = CuredDiseases()
# print("Current state of Cures:",cdc.db)
# cdc.cure(cdc.red)
# print("Current state of Cures:",cdc.db)
# cdc.cure(cdc.yellow)
# cdc.cure(cdc.black)
# cdc.eradicate(cdc.black)
# print("Current state of Cures:",cdc.db)
# print(cdc.checkCure())


# class Outbreaks(Counter):
#     pass
#
#
# class InfectionRate(Counter):
#     def __init__(self):
#         self.value = 0
#         infection_level_list = [2, 2, 2, 3, 3, 4, 4]
#
#
#     def return_current_infection_level(self):
#         return infection_level_list[infection_step]
#
#     def __str__(self):
#         return return_current_infection_level

# irc = InfectionRate()
# print(irc.return_current_infection_level())



