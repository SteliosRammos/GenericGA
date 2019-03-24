import random
import config
import numpy as np

class AbstractIndividual:
    def get_encoding(self):
        pass

    def get_fitness(self):
        pass


class KnapsackIndividual(AbstractIndividual):

    def __init__(self, pop_id, ind_id, items, encoding=None):
        self.pop_id = pop_id
        self.ind_id = ind_id
        self.items = items

        if pop_id == 0:
            self.encoding = [1 if random.random() > 0.5 else 0 for item in items]
        else:
            self.encoding = encoding

    def get_encoding(self):
        return self.encoding

    def get_fitness(self):

        weight = 0
        value = 0

        for i in range(0, len(self.encoding)):
            weight += (self.encoding[i] * self.items[i][1])
            value += (self.encoding[i] * self.items[i][0])

        if weight > config.max_weight:
            return 0
        else:
            return value


class TSPIndividual(AbstractIndividual):
    def __init__(self, pop_id, ind_id, cities, encoding=None):
        self.pop_id = pop_id
        self.ind_id = ind_id
        self.cities = cities

        if pop_id == 0:
            self.encoding = np.random.choice(cities, len(cities), replace=False)
        else:
            self.encoding = encoding

    def get_encoding(self):
        return self.encoding

    def get_fitness(self):

        cities = self.encoding
        path_distance = 0
        fitness = 0
        # for city in cities:
        #     print(city.ind_id)

        for i in range(0, len(cities)):
            if i < len(cities)-1:
                path_distance += cities[i].distance(cities[i+1])
            else:
                path_distance += cities[i].distance(cities[0])

        if path_distance != 0:
            fitness = 1 / float(path_distance)

        return fitness
