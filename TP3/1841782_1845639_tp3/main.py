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
def bfs_glouton(matrice_adjacence, infectes):

    solution = []

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

                        matrice_adjacence[edge_1, p_relation] = False
                        matrice_adjacence[p_relation, edge_1] = False

                        c_related_infected = np.delete(c_related_infected, rand_infected)

                        print(edge_1, p_relation)
                        solution.append((edge_1, p_relation))

    return solution

def forward(matrice_adjacence, set_sains, set_infectes):
    """Simule une itération de contamination
    """

    # Flag d'atteinte du point fixe
    done = False

    # On mémorise les individus sains et infectés à l'itération précédente
    anciens_infectes = set_infectes.copy()
    anciens_sains = set_sains.copy()

    for sommet_sain in anciens_sains:
        nb_voisins_infectes = 0
        for node, is_neighbor in enumerate(matrice_adjacence[sommet_sain]):
            if is_neighbor and node in anciens_infectes:
                nb_voisins_infectes += 1
                if nb_voisins_infectes == k:
                    set_sains.remove(sommet_sain)
                    set_infectes.add(sommet_sain)
                    break

    if len(set_infectes) == len(anciens_infectes):
        done = True

    return set_sains, set_infectes, done


if __name__=="__main__":

    k = int(sys.argv[sys.argv.index("-k") + 1])
    path = sys.argv[sys.argv.index("-e") + 1]

    nombre_sommets, nombre_infectes, matrice_adjacence, infectes = exemplaire_load(path)

    show_best_result_runtime = sys.argv.count("-p") > 0

    solution = bfs_glouton(matrice_adjacence, infectes)

    infectes = set(infectes)
    sains = set(range(nombre_sommets)).difference(infectes)

    best_solution_value = len(solution)
    c_solution = copy.deepcopy(solution)

    # Heuristique d'amélioration locale du bfs_glouton
    while(True):
        # init var
        has_solution = False
        last_readded_relation = None # Tuple (edge1, edge2)

        while(not has_solution):

            c_infectes = infectes.copy()
            c_sains = sains.copy()

            try:
                rand_edge = randint(0, len(c_solution) - 1)
            except:
                has_solution = True
                continue

            last_readded_relation = c_solution[rand_edge]
            matrice_adjacence[last_readded_relation[0], last_readded_relation[1]] = True
            matrice_adjacence[last_readded_relation[1], last_readded_relation[0]] = True

            # Propagation
            done = False
            while not done:
                c_sains, c_infectes, done = forward(matrice_adjacence, c_sains, c_infectes)

            # Si plus de la moitié de la population est infectée, la solution est invalide
            if len(c_infectes) > nombre_sommets / 2:
                has_solution = True
            else:
                c_solution = np.delete(c_solution, rand_edge)

        new_sol_value = len(c_solution)
        if new_sol_value < best_solution_value:
            print()
            for sol in c_solution:
                print(sol[0], sol[1])

            best_solution_value = new_sol_value

        c_solution = copy.deepcopy(solution)

        for sol in c_solution:
            matrice_adjacence[sol[0], sol[1]] = False
            matrice_adjacence[sol[1], sol[0]] = False
            