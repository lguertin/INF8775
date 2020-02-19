import numpy as np
import os


def create_partition():
    tailles_exemplaires = [1000, 3000, 10000, 30000,
                           100000, 300000, 1000000, 3000000, 6000000, 8000000]
    try:
        os.mkdir("exemplaires")
        for nb_notes in tailles_exemplaires:
            for i in range(1, 11):
                with open(os.path.join("exemplaires", f"ex_{nb_notes}_{i}.txt"), 'w') as f:
                    print(str(nb_notes), file=f)
                    notes = np.random.randint(
                        0, 24, size=nb_notes, dtype='int64')
                    print(' '.join([str(n) for n in notes]), file=f)
    except:
        print("Les exemplaires ont déjà été créés. Si vous voulez les créer à nouveau, supprimer le dossier 'exemplaires'.")


if __name__ == '__main__':
    create_partition()
