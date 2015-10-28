__author__ = 'JMullens'

class CityDB(object):
    def __init__(self):
        pass

    def infect(self, city, color, amount=1):
        city['city_infection_counter'][color] += amount
        print("%s was infected with %s %s cubes." % (city["name"], amount, color))

    def set_infection(self, city, color, amount=0):
        city['city_infection_counter'][color] = amount
        print("%s %s Infection Counter set to %s" % (city['name'], color, amount))

    def get_infection(self, target):
        return target['city_infection_counter']

    def outbreak(self):
        pass

# ## Infection Example
# city = CityDB()
# print(algiers['name'], algiers['city_infection_counter'])
# city.infect(algiers, 'yellow', 1)
# print(algiers['name'], algiers['city_infection_counter'])
# city.infect(algiers, 'yellow', 1)
# city.infect(algiers, 'black', 1)
# print(algiers['name'], algiers['city_infection_counter'])
# city.set_infection(algiers, 'red', 3)
# print(algiers['name'], algiers['city_infection_counter'])

# city = CityDB()
# print(city.get_infection(atlanta))
# city.infect(city.atlanta, 'blue', 3)
# print(city.get_infection(city.atlanta))



