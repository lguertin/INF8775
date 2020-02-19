import math, sys, time
import numpy as np
import copy

def notes_load(path):
    f = open(path, "r")
    size = int(f.readline())
    notes = np.array(f.readline().split(' '), dtype=int)
    f.close()
    return size, notes

def glouton(size, notes, cout):
    s = []
    c = copy.deepcopy(cout)

    d = np.unravel_index(np.argmin(c[notes[0], :, notes[1], :], axis=None), (5, 5))

    s.append((d[0], 0))
    s.append((d[1], c[notes[0], d[0], notes[1], d[1]]))
    d1 = d[1]

    while len(c) > 0 and len(s) < size - 1:
        i = len(s)
        d2 = np.argmin(c[notes[i], d1, notes[i + 1], :], axis=None)
        s.append((d2, c[notes[i], d1, notes[i + 1], d2]))
        d1 = d2

    return s

if __name__=="__main__":

    algo = sys.argv[sys.argv.index("-a") + 1]
    path = sys.argv[sys.argv.index("-e") + 1]

    load_file = np.loadtxt('cout_transition.txt', dtype=int)
    cout_transition = load_file.reshape((24, 5, 24, 5))

    size, notes = notes_load(path)

    s = [] # List tuple (doigt, cout)

    begin = time.time()
    if algo == "glouton":
        s = glouton(size, notes, cout_transition)
    elif algo == "dp":
        pass
    else:
        pass

    if sys.argv.count("-t"):
        print((time.time() - begin) * 1000)

    d, c = map(list, zip(*s))

    if sys.argv.count("-p"):
        print(np.sum(c))

    if sys.argv.count("-c"):
        print(*d)