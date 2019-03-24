import matplotlib.pyplot as plt


class GeneticAlgorithm:

    populations = []
    current_pop = None

    def __init__(self, world, mutation_prob, verbose, testing):
        '''
        :param world: World Class defining the problem parameters
        :param mutation_prob: probability of mutating
        :param verbose: True for console prints
        :param testing: True to return whether true optimality was reached
        '''
        self.world = world
        self.mutation_prob = mutation_prob
        self.verbose = verbose
        self.testing = testing
        self.test_iterations = 0
        # Create initial population
        self.current_pop = world.create_population(world.pop_size, pop_id=0, genes=world.genes)
        self.populations.append(self.current_pop)

    def evolve(self):
        # print("######################### STARTING EVOLUTION #########################\n ")

        world = self.world

        while not self.terminate():

            current_pop = self.current_pop

            # Generate a new population, ie: generate offsprings through cross-over and mutations
            new_individuals = current_pop.generate_offsprings(current_pop.pop_size, world.selection, world.cross_over, self.mutation_prob)
            new_pop = world.create_population(world.pop_size, current_pop.pop_id+1, genes=world.genes, individuals=new_individuals)

            # Add new population in population arrays
            self.populations.append(new_pop)
            self.current_pop = new_pop

        pop_id = self.current_pop.pop_id
        best_fitness = 0

        for individual in self.current_pop.individuals:
            fitness = individual.get_fitness()

            if fitness > best_fitness:
                best_fitness = fitness

        if self.verbose:
            optimal_ind = world.optimal_ind.get_encoding()
            coordinates = []
            xs = []
            ys = []

            for city in optimal_ind:
                coordinates.append(city.get_coordinates())
                xs.append(city.x)
                ys.append(city.y)

            plt.plot(xs, ys)
            plt.scatter(xs, ys)
            plt.show()
            print(
                "Evolution Completed. \n",
                "Optimal Fitness: {} \n".format(world.optimal_fitness),
                "Optimal Individual: {}\n".format(coordinates),
                "Found in generation: {}\n".format(world.optimal_pop.pop_id)
            )

        if self.testing:
            found_optimal = False
            true_optimal = world.get_true_optimal()
            if world.optimal_fitness == true_optimal:
                found_optimal = True

            return world.optimal_pop.pop_id, world.optimal_fitness, found_optimal

        if world.optimal_pop is None:
            return -1, world.optimal_fitness

        return world.optimal_pop.pop_id, world.optimal_fitness

    def terminate(self):
        terminate = self.world.termination_func(self.current_pop)
        return terminate
