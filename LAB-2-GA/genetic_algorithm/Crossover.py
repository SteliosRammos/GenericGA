import numpy as np
import random


class Crossovers:

    def __init__(self, cross_prob):
        self.cross_prob = cross_prob

    def single_point_cross(self, ind_a, ind_b):

        prob_same = random.random()

        if prob_same > self.cross_prob:
            # print('Same')
            child_a = ind_a.get_encoding()
            child_b = ind_b.get_encoding()
        else:
            # perform single point cross
            cross_point = random.randint(0, len(ind_a.get_encoding())-1)

            ind_a = ind_a.get_encoding()
            ind_b = ind_b.get_encoding()

            # print('Cross_point:', cross_point)
            child_a = ind_a[:cross_point]+ind_b[cross_point:]
            child_b = ind_b[:cross_point]+ind_a[cross_point:]

        return child_a, child_b

    def ordered_crossover(self, ind_a, ind_b):

        ind_a = ind_a.get_encoding()
        ind_b = ind_b.get_encoding()
        children = []

        for i in range(0, 2):
            child = []
            child_p1 = []
            child_p2 = []

            gene_a = np.random.randint(0, len(ind_a)-1)
            gene_b = gene_a

            while gene_a == gene_b:
                gene_b = np.random.randint(0, len(ind_b)-1)

            start_gene = min(gene_a, gene_b)
            end_gene = max(gene_a, gene_b)

            for i in range(start_gene, end_gene):
                child_p1.append(ind_a[i])

            child_p2 = [item for item in ind_b if item not in child_p1]

            # print(child_p1, child_p2)
            child = child_p1 + child_p2
            children.append(child)

        # print(children)
        return children
