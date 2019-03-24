import numpy as np


class RandomSelection:

    def select(self, mating_pool):
        chosen = [None, None]
        # np.random.seed(1)

        for i in range(0, 2):
            r_ind = np.random.randint(0, len(mating_pool) - 1)
            chosen[i] = r_ind

        return chosen


class RouletteSelection:
    def __init__(self, t):
        self.t = t
        # self.f = []
        # self.sum_f = 0

    def get_indiv_prob(self, mating_pool):

        fitnesses = [np.exp(individual.get_fitness() / self.t) for individual in mating_pool]
        total_fitnesses = np.sum(fitnesses)

        individual_probs = np.zeros(len(mating_pool))
        # individual_probs = 0
        i = 0
        for fitness in fitnesses:
            individual_probs[i] = fitness / total_fitnesses
            i += 1

        return individual_probs

    def select(self, mating_pool):
        pool = mating_pool
        chosen = [None, None]
        indiv_probas = self.get_indiv_prob(pool)
        roulette = indiv_probas.cumsum()
        # np.random.seed(1)

        for i in range(0, 2):
            r = np.random.rand()

            for j in range(0, len(roulette)):
                if r <= roulette[j]:
                    chosen[i] = j
                    # pool.pop(j)
                    break

        return chosen