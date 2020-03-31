import math, sys, time, copy
import numpy as np
from random import randint

def notes_load(path):
    f = open(path, "r")
    size = int(f.readline())
    notes = np.array(f.readline().split(' '), dtype=int)
    f.close()
    return size, notes

def glouton(size, notes, cout):
    s = []

    d = np.unravel_index(np.argmin(cout[notes[0], :, notes[1], :], axis=None), (5, 5))

    s.append((d[0], 0))
    s.append((d[1], cout[notes[0], d[0], notes[1], d[1]]))
    d1 = d[1]

    while len(s) < size - 1:
        i = len(s)
        d2 = np.argmin(cout[notes[i], d1, notes[i + 1], :], axis=None)
        s.append((d2, cout[notes[i], d1, notes[i + 1], d2]))
        d1 = d2

    d, c = map(list, zip(*s))

    return d, np.sum(c)

def dynamic_prog(size, notes, cout):
    c = np.zeros((5, size), dtype=int)
    d = np.zeros((5, size), dtype=int)

    for i in range(size - 2, -1, -1):
        for j in range(5):
            tmp = cout[notes[i], j, notes[i + 1], :] + c[:, i + 1]
            c[j][i] = np.min(tmp)
            d[j][i] = np.argmin(tmp)

    doigts = []
    curr_idx = np.argmin(c[:, 0])
    doigts.append(curr_idx)

    cout_transition = c[curr_idx, 0]

    for i in range(size - 1):
        curr_idx = d[curr_idx, i]
        doigts.append(curr_idx)

    return doigts, cout_transition

def neighbors(size, notes, cout):
    d, c = glouton(size, notes, cout)

    best_d = d

    n_iterations = (int)(size * 0.1)
    for _ in range (n_iterations):
        rand_d = randint(0, 4)
        rand_n = randint(0, size - 1)
        
        cost_removed = 0
        cost_added = 0

        if rand_d > 0:
            cost_removed += cout[notes[rand_n - 1], best_d[rand_n - 1], notes[rand_n], best_d[rand_d]]
            cost_added += cout[notes[rand_n - 1], best_d[rand_n - 1], notes[rand_n], rand_d]

        if rand_d < size - 1:
            cost_removed += cout[notes[rand_n], best_d[rand_n], notes[rand_n + 1], best_d[rand_d + 1]]
            cost_added += cout[notes[rand_n], rand_d, notes[rand_n + 1], best_d[rand_n + 1]]

        if cost_added < cost_removed:
            best_d[rand_n] = rand_d
            c = c - cost_removed + cost_added

    return best_d, c

if __name__=="__main__":

    algo = sys.argv[sys.argv.index("-a") + 1]
    path = sys.argv[sys.argv.index("-e") + 1]

    load_file = np.loadtxt('cout_transition.txt', dtype=int)
    cout_transition = load_file.reshape((24, 5, 24, 5))

    size, notes = notes_load(path)

    s = [] # List tuple (doigt, cout)

    begin = time.time()
    if algo == "glouton":
        d, c = glouton(size, notes, cout_transition)
    elif algo == "dp":
        d, c = dynamic_prog(size, notes, cout_transition)
    else:
        d, c = neighbors(size, notes, cout_transition)

    if sys.argv.count("-t"):
        print((time.time() - begin) * 1000)

    if sys.argv.count("-p"):
        print(c)

    if sys.argv.count("-c"):
        print(*d)