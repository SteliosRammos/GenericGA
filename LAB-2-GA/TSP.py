from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm
from genetic_algorithm.World import TSPWorld
from genetic_algorithm.Crossover import Crossovers
from genetic_algorithm.Selection import RouletteSelection, RandomSelection

import numpy as np
import matplotlib.pyplot as plt

########## RUN TESTS BY UNCOMMENTING THE PIECE OF CODE OF THE TEST YOU WISH TO RUN ##########
'''
This implementation of the Traveling Salesperson is inspired from the Eric Stoltz tutorial that can be found here:
https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35

Eric's tutorial holds reference to the following two github repositories: 
https://gist.github.com/turbofart/3428880
https://gist.github.com/NicolleLouis/d4f88d5bd566298d4279bcb69934f51d

Some occurrences of the code on those repositories might have found its way here and/or inspired some of the choices 
made during the implementation of our Genetic Algorithm for the traveling salesperson problem. 
'''


# Single run
# pop_size = 200
# selection = RandomSelection()
# cross_over = Crossovers(0.9)
# tsp_world = TSPWorld(pop_size, selection, cross_over, max_staling=1500)
# genetic_alg = GeneticAlgorithm(
#     world=tsp_world,
#     mutation_prob=0.05,
#     verbose=True,
#     testing=True
# )
# pop_id, opt_fitness, found_optimal = genetic_alg.evolve()

# # A. Test mutation probability change in convergence/fitness
pop_size = 500
selection = RandomSelection()
cross_over = Crossovers(0.7)
fig, ax = plt.subplots()
gens_to_convergence = []
optimals_found = []
mutation_probabilities = np.arange(1, 10)/100

for i in mutation_probabilities:
    convergence = []
    true_optimals = 0
    for j in range(0, 10):
        tsp_world = TSPWorld(pop_size, selection, cross_over, max_staling=1000)
        genetic_alg = GeneticAlgorithm(
            world=tsp_world,
            mutation_prob=i,
            verbose=False,
            testing=True
        )
        pop_id, opt_fitness, found_optimal = genetic_alg.evolve()
        convergence.append(pop_id)
        if found_optimal:
            true_optimals += 1
    optimals_found.append(true_optimals)
    gens_to_convergence.append(convergence)

print(optimals_found)
ax.boxplot(gens_to_convergence, labels=mutation_probabilities)
plt.xlabel('Mutation Rate')
plt.ylabel('Number of Generations To Local Optimum')
plt.title('Effect of mutation rate on convergence')
plt.savefig("figures/tsp/mutation_prob_convergence.png", pad_inches=0.2)
plt.show()
