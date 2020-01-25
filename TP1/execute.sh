#!/bin/bash

for n in 1 2 3 4 5
do
    echo "Multiplication conventionnelle 2^${n}x2^${n}"
    for i in 1 2 3 4 5
    do
        for j in 1 2 3 4 5
        do
        ./tp.sh -a conv -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -t
        done
    done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'

    echo "Multiplication diviser-pour-regner 2^${n}x2^${n}"
    for i in 1 2 3 4 5
    do
        for j in 1 2 3 4 5
        do
        ./tp.sh -a strassen -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -t
        done
    done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'

    echo "Multiplication diviser-pour-regner avec seuil 2^${n}x2^${n}"
    for i in 1 2 3 4 5
    do
        for j in 1 2 3 4 5
        do
        ./tp.sh -a strassenSeuil -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -t
        done
    done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'

    # Envois une erreur si le resultat est different
    for i in 1 2 3 4 5
    do
        for j in 1 2 3 4 5
        do
        diff -q <(./tp.sh -a conv -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -p) \
        <(./tp.sh -a strassen -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -p)
        diff -q <(./tp.sh -a strassen -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -p) \
        <(./tp.sh -a strassenSeuil -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -p)
        done
    done
done