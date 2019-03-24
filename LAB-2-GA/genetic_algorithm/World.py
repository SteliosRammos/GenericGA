import random
import config
import math
from genetic_algorithm.Population import KnapsackPopulation, TSPPopulation
from genetic_algorithm.City import City


class AbstractWorld:

    def termination_func(self, population):
        pass

    def create_population(self,  pop_size, pop_id, genes, individuals):
        pass


class KnapsackWorld(AbstractWorld):

    def __init__(self, pop_size, selection, cross_over, max_weight, max_staling):
        '''

        :param pop_size: population size
        :param selection: Selection Class
        :param cross_over: Crossover Class
        :param max_weight: Maximum weight of knapsack
        :param max_staling: Maximum number of generations after optimum was last updated
        '''
        # Initialise seed for reproducibility
        random.seed(1)

        # Initialize parameters
        config.max_weight = max_weight
        self.pop_size = pop_size
        self.genes = [[random.randint(1, 10), random.randint(1, 10)] for i in range(0, 10)]
        self.max_staling = max_staling
        self.unchanged = 0
        self.optimal_fitness = 0
        self.optimal_ind = None
        self.optimal_pop = None
        self.selection = selection
        self.cross_over = cross_over
        self.overweight_pop = False

    def termination_func(self, population):

        # print(population.individuals)
        over_weight = 0
        new_optimal = 0

        for individual in population.individuals:

            encoding = individual.get_encoding()
            value = individual.get_fitness()
            weight = 0

            for i in range(0, len(encoding)):
                weight += encoding[i] * self.genes[i][1]

            if weight <= config.max_weight:
                over_weight += 1

            if value > new_optimal:
                new_optimal = value
                new_optimal_ind = individual
                new_optimal_ind_pop = population

        if new_optimal > self.optimal_fitness:
            self.optimal_fitness = new_optimal
            self.optimal_ind = new_optimal_ind
            self.optimal_pop = new_optimal_ind_pop
            self.unchanged = 0
        else:
            self.unchanged += 1

        if over_weight > int(len(population.individuals)*0.1):
            # print('Fail! Overweight population...')
            self.overweight_pop = True
            return True

        if self.unchanged >= self.max_staling:
            # print('Converged!')
            return True

        return False

    def create_population(self,  pop_size, pop_id, genes, individuals=None):
        population = KnapsackPopulation(pop_size, pop_id, genes, individuals)
        return population

    def get_true_optimal(self):
        pass


class TSPWorld(AbstractWorld):

    def __init__(self, pop_size, selection, cross_over, max_staling):

        # Initialise seed for reproducibility
        random.seed(1)

        # Initialize parameters
        self.pop_size = pop_size
        self.genes = self.create_cities(10)

        # for gene in self.genes:
        #     print(gene.get_coordinates())
        # exit()
        self.selection = selection
        self.cross_over = cross_over
        self.max_staling = max_staling
        self.unchanged = 0
        self.optimal_fitness = 0
        self.optimal_ind = None
        self.optimal_pop = None

    def termination_func(self, population):

        new_optimal = 0

        for individual in population.individuals:

            # encoding = individual.get_encoding()
            value = individual.get_fitness()

            if value > new_optimal:
                new_optimal = value
                new_optimal_ind = individual
                new_optimal_ind_pop = population

        if new_optimal > self.optimal_fitness:
            self.optimal_fitness = new_optimal
            self.optimal_ind = new_optimal_ind
            self.optimal_pop = new_optimal_ind_pop
            self.unchanged = 0
        else:
            self.unchanged += 1

        if self.unchanged >= self.max_staling:
            # print('Converged!')
            return True

        return False

    def create_population(self,  pop_size, pop_id, genes, individuals=None):
        population = TSPPopulation(pop_size, pop_id, genes, individuals)
        return population

    def create_cities(self, n_cities):
        x_coordinates = []
        y_coordinates = []

        for index in range(n_cities):
            x_coordinates.append(math.cos((index * 2 * math.pi) / n_cities))
            y_coordinates.append(math.sin((index * 2 * math.pi) / n_cities))

        cities = [City(x_coordinates[i], y_coordinates[i]) for i in range(0, n_cities)]

        return cities

    def get_true_optimal(self):

        cities = self.genes
        path_distance = 0
        fitness = 0
        # for city in cities:
        #     print(city.ind_id)

        for i in range(0, len(cities)):
            if i < len(cities) - 1:
                path_distance += cities[i].distance(cities[i + 1])
            else:
                path_distance += cities[i].distance(cities[0])

        if path_distance != 0:
            fitness = 1 / float(path_distance)

        return fitness
