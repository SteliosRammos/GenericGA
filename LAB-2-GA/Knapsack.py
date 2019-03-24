from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm
from genetic_algorithm.World import KnapsackWorld
from genetic_algorithm.Crossover import Crossovers
from genetic_algorithm.Selection import RouletteSelection, RandomSelection

import numpy as np
import matplotlib.pyplot as plt

########## RUN TESTS BY UNCOMMENTING THE PIECE OF CODE OF THE TEST YOU WISH TO RUN ##########

# # A. Test mutation probability change in convergence/fitness
# pop_size = 100
# selection = RandomSelection()
# cross_over = Crossovers(0.7)
# fig, ax = plt.subplots()
# gens_to_convergence = []
# mutation_probabilities = np.arange(1, 10)/100
# for i in mutation_probabilities:
#     convergence = []
#     for j in range(0, 10):
#         knapsack_world = KnapsackWorld(pop_size, selection, cross_over, max_weight=8, max_staling=500)
#         genetic_alg = GeneticAlgorithm(
#             world=knapsack_world,
#             mutation_prob=i,
#             verbose=True
#         )
#         pop_id, opt_fitness = genetic_alg.evolve()
#         convergence.append(pop_id)
#     gens_to_convergence.append(convergence)
#
# ax.boxplot(gens_to_convergence, labels=mutation_probabilities)
# plt.xlabel('Mutation Rate')
# plt.ylabel('Number of Generations To Local Optimum')
# plt.title('Effect of mutation rate on convergence')
# plt.savefig("figures/ks/mutation_prob_convergence.png", pad_inches=0.2)
# plt.show()

# # B. Test cross over probability change in convergence/fitness
# pop_size = 100
# selection = RandomSelection()
# fig, ax = plt.subplots()
# gens_to_convergence = []
# crossover_probabilities = np.arange(5, 10)/10
# for i in crossover_probabilities:
#     convergence = []
#     cross_over = Crossovers(i)
#     for j in range(0, 100):
#         knapsack_world = KnapsackWorld(pop_size, selection, cross_over, max_weight=8, max_staling=500)
#         genetic_alg = GeneticAlgorithm(
#             world=knapsack_world,
#             mutation_prob=0.01,
#             verbose=False
#         )
#         pop_id, opt_fitness = genetic_alg.evolve()
#         convergence.append(pop_id)
#     gens_to_convergence.append(convergence)
#
# ax.boxplot(gens_to_convergence, labels=crossover_probabilities)
# plt.xlabel('Cross-Over Probability')
# plt.ylabel('Number of Generations To Local Optimum')
# plt.title('Effect of cross-over probability on convergence')
# plt.savefig("figures/ks/crossover_prob_convergence.png")
# plt.show()

# # C. Test selection type on convergence
# fig, ax = plt.subplots()
# gens_to_convergence = []
# pop_size = 100
# cross_over = Crossovers(0.7)
# temperatures = np.arange(1, 6)/10
# for i in temperatures:
#     convergence = []
#     selection = RouletteSelection(i)
#     for j in range(0, 100):
#         knapsack_world = KnapsackWorld(pop_size, selection, cross_over, max_weight=8, max_staling=500)
#         genetic_alg = GeneticAlgorithm(
#             world=knapsack_world,
#             mutation_prob=0.01,
#             verbose=False
#         )
#         pop_id, opt_fitness = genetic_alg.evolve()
#         convergence.append(pop_id)
#     gens_to_convergence.append(convergence)
#
# ax.boxplot(gens_to_convergence, labels=temperatures)
# plt.xlabel('Temperature')
# plt.ylabel('Number of Generations To Local Optimum')
# plt.title('Effect of Roulette Selection Parameter T on convergence')
# plt.savefig("figures/ks/roulette_selection_convergence.png")
# plt.show()

# # D. Test selection type on convergence
# fig, ax = plt.subplots()
# gens_to_convergence = []
# cross_over = Crossovers(0.7)
# selection = RouletteSelection(0.1)
# population_sizes = [10, 50, 100, 500]
#
# for pop_size in population_sizes:
#     convergence = []
#
#     for j in range(0, 100):
#         knapsack_world = KnapsackWorld(pop_size, selection, cross_over, max_weight=8, max_staling=500)
#         genetic_alg = GeneticAlgorithm(
#             world=knapsack_world,
#             mutation_prob=0.01,
#             verbose=False
#         )
#         pop_id, opt_fitness = genetic_alg.evolve()
#         convergence.append(pop_id)
#     gens_to_convergence.append(convergence)
#
# ax.boxplot(gens_to_convergence, labels=population_sizes)
# plt.xlabel('Population Size')
# plt.ylabel('Number of Generations To Local Optimum')
# plt.title('Effect of Population Size on convergence')
# plt.savefig("figures/ks/pop_size_convergence.png")
# plt.show()


