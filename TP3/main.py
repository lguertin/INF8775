import math, sys, copy
import numpy as np
from random import randint

def exemplaire_load(path):

    f = open(path, "r")

    nombre_sommets, nombre_infectes = [int(i) for i in f.readline().strip().split(" ")]
    matrice_adjacence = np.zeros((nombre_sommets, nombre_sommets), dtype=bool)

    for i in range(nombre_sommets):
        matrice_adjacence[i] = np.fromiter(map(int, f.readline().strip().split(' ')), bool)

    infectes = [int(i) for i in f.readline().strip().split(" ")]

    f.close()

    return nombre_sommets, nombre_infectes, matrice_adjacence, infectes

def sherwood(matrice_adjacence, infectes, k):
    rand_infected = randint(0, len(infectes) - 1)

    edge_1 = infectes[rand_infected]

    relations = np.where(matrice_adjacence[edge_1])[0]

    if (len(relations) > k):
        edge_2 = np.random.choice(relations)

        matrice_adjacence[edge_1, edge_2] = False
        matrice_adjacence[edge_2, edge_1] = False

        print(edge_1, edge_2)

# Ne pas considerer les noeuds avec moins de k relations (k true)

# Starts with infected node, goes in uninfected nodes, check if it is touching more than k infected nodes
# Parent : infected node
def search(parent, current_node, nombre_sommets, nombre_infectes, matrice_adjacence, infectes):
    pass


# Quand k arretes de personnes infectes touchent un autre sommet

if __name__=="__main__":

    k = int(sys.argv[sys.argv.index("-k") + 1])
    path = sys.argv[sys.argv.index("-e") + 1]

    nombre_sommets, nombre_infectes, matrice_adjacence, infectes = exemplaire_load(path)

    show_best_result_runtime = sys.argv.count("-p") > 0

    # TO REMOVE START
    # Glouton removing all edges on the infected nodes
    # sol_max = 0
    # for i in infectes:
    #     # print(np.where(matrice_adjacence[i])[0])
    #     sol_max += len(np.where(matrice_adjacence[i])[0])
    # print("Maximum relations to remove :", sol_max)
    # TO REMOVE END

    for i in range(nombre_infectes * k * 5):
        sherwood(matrice_adjacence, infectes, k)
    
    for infecte in infectes:

        # Parent est en relation avec :
        p_relations = np.where(matrice_adjacence[infecte])[0]
        for p_relation in p_relations:
            if p_relation not in infectes:
                # Enfant est en relation avec:
                child_relations = np.where(matrice_adjacence[p_relation])[0]

                if len(child_relations) >= k:
                    c_related_infected = np.intersect1d(child_relations, infectes)

                    while len(c_related_infected) >= k:
                        rand_infected = randint(0, len(c_related_infected) - 1)

                        edge_1 = c_related_infected[rand_infected]

                        # print(matrice_adjacence[edge_1, p_relation])
                        # print(matrice_adjacence[p_relation, edge_1])
                        # print(c_related_infected, child_relations, infectes)
                        # print(child_relations)
                        # print(matrice_adjacence[p_relation])
                        # input()

                        matrice_adjacence[edge_1, p_relation] = False
                        matrice_adjacence[p_relation, edge_1] = False

                        c_related_infected = np.delete(c_related_infected, rand_infected)

                        print(edge_1, p_relation)


    # TO REMOVE START
    # Get how much better is our solution from glouton
    # sol_max_2 = 0
    # for i in infectes:
    #     print(np.where(matrice_adjacence[i])[0])
    #     sol_max_2 += len(np.where(matrice_adjacence[i])[0])
    # print("Relations removed :", sol_max - sol_max_2)
    # TO REMOVE END


    # search(infecte, relation, nombre_sommets, nombre_infectes, matrice_adjacence, infectes)


    # while True:
    #     pass


# (t / 50 * n) - 1 ou t est le nombre de cas tolerees
# =>probleme similaire au 4 reines (approche probabiliste + backtrack)