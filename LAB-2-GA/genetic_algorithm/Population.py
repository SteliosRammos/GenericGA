from genetic_algorithm.Individual import KnapsackIndividual, TSPIndividual
import random


class AbsctractPopulation:

    def generate_offsprings(self, n, selection, cross_over, mutation_prob):
        pass

    def mutate(self, mutation_prob, encoding):
        pass


class KnapsackPopulation(AbsctractPopulation):
    individuals = []

    def __init__(self, pop_size, pop_id, items, individuals=None):
        self.pop_size = pop_size
        self.pop_id = pop_id
        self.items = items
        # self.genetic_alg = genetic_alg
        if pop_id == 0:
            for i in range(0, self.pop_size):
                individual = KnapsackIndividual(pop_id=pop_id, ind_id=i, items=items)
                self.individuals.append(individual)

        else:
            self.individuals = individuals

    def generate_offsprings(self, n, selection, cross_over, mutation_prob):

        # mating_pool = self.generate_mating_pool()
        mating_pool = self.individuals
        offsprings = []
        chosen = 0
        i = 0

        while len(mating_pool) != 0 and chosen < n:
            # print("ITERATION ", i)
            # print('Pool size:', len(mating_pool))
            # print("Generating offsprings {} and {} \n".format(chosen, chosen +1))
            index_a, index_b = selection.select(mating_pool)
            indiv_a, indiv_b = mating_pool[index_a], mating_pool[index_b]

            # print("Popping index {} and {} from mating pool".format(index_a, index_b))
            mating_pool.pop(index_a)
            if index_a > index_b:
                mating_pool.pop(index_b)
            else:
                mating_pool.pop(index_b-1)

            # print("Pre-crossover: \n indiv_a: {} | indiv_b: {}".format(indiv_a.get_encoding(), indiv_b.get_encoding()))
            encoding_a, encoding_b = cross_over.single_point_cross(indiv_a, indiv_b)

            encoding_a = self.mutate(mutation_prob, encoding_a)
            encoding_b = self.mutate(mutation_prob, encoding_b)

            child_a = KnapsackIndividual(self.pop_id, chosen, encoding=encoding_a, items=self.items)
            child_b = KnapsackIndividual(self.pop_id, chosen+1, encoding=encoding_b, items=self.items)

            # print("Pre-crossover: \n child_a: {} | child_b: {}".format(child_a.get_encoding(), child_b.get_encoding()))
            offsprings.append(child_a)
            offsprings.append(child_b)

            i += 1
            chosen += 2

        return offsprings

    def mutate(self, mutation_prob, encoding):
        new_encoding = []
        for i in range(0, len(encoding)):
            r = random.random()

            if r < mutation_prob:
                if encoding[i] == 0:
                    new_encoding.append(1)
                else:
                    new_encoding.append(0)
            else:
                new_encoding.append(encoding[i])

        return new_encoding


class TSPPopulation:

    individuals = []

    def __init__(self, pop_size, pop_id, cities, individuals=None):
        self.pop_size = pop_size
        self.pop_id = pop_id
        self.cities = cities

        if pop_id == 0:
            for i in range(0, self.pop_size):
                individual = TSPIndividual(pop_id=pop_id, ind_id=i, cities=cities)
                self.individuals.append(individual)

        else:
            self.individuals = individuals

    def generate_offsprings(self, n, selection, cross_over, mutation_prob):

        mating_pool = self.individuals
        offsprings = []
        chosen = 0
        i = 0

        while len(mating_pool) != 0 and chosen < n:
            # print("ITERATION ", i)
            index_a, index_b = selection.select(mating_pool)
            indiv_a, indiv_b = mating_pool[index_a], mating_pool[index_b]

            # print("Popping index {} and {} from mating pool".format(index_a, index_b))
            mating_pool.pop(index_a)
            if index_a > index_b:
                mating_pool.pop(index_b)
            else:
                mating_pool.pop(index_b-1)

            # print("Pre-crossover: \n indiv_a: {} | indiv_b: {}".format(indiv_a.get_encoding(), indiv_b.get_encoding()))
            encoding_a, encoding_b = cross_over.ordered_crossover(indiv_a, indiv_b)

            encoding_a = self.mutate(mutation_prob, encoding_a)
            encoding_b = self.mutate(mutation_prob, encoding_b)

            child_a = TSPIndividual(self.pop_id, chosen, encoding=encoding_a, cities=self.cities)
            child_b = TSPIndividual(self.pop_id, chosen+1, encoding=encoding_b, cities=self.cities)

            # print("Pre-crossover: \n child_a: {} | child_b: {}".format(child_a.get_encoding(), child_b.get_encoding()))
            offsprings.append(child_a)
            offsprings.append(child_b)

            i += 1
            chosen += 2

        return offsprings

    def mutate(self, mutation_prob, encoding):

        r = random.random()
        new_encoding = encoding.copy()

        if r < mutation_prob:
            swap_a = random.randint(0, len(encoding)-1)
            swap_b = swap_a

            while swap_a == swap_b:
                swap_b = random.randint(0, len(encoding)-1)

            new_encoding[swap_a] = encoding[swap_b]
            new_encoding[swap_b] = encoding[swap_a]

        return new_encoding
