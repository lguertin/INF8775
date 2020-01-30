#!/bin/bash

for n in {1..12}
do
    echo "Multiplication conventionnelle 2^${n}x2^${n}"
    for (( i = 1; i <= 5; i++ ))
    do
        for (( j = i ; j <= 5; j++ ))
        do
        ./tp.sh -a conv -e1 ./gen_matrix/ex_${n}.${i} -e2 ./gen_matrix/ex_${n}.${j} -t
        done
    done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'

    echo "Multiplication diviser-pour-regner 2^${n}x2^${n}"
    for (( i = 1; i <= 5; i++ ))
    do
        for (( j = i ; j <= 5; j++ ))
        do
        ./tp.sh -a strassen -e1 ./gen_matrix/ex_${n}.${i} -e2 ./gen_matrix/ex_${n}.${j} -t
        done
    done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'

    echo "Multiplication diviser-pour-regner avec seuil 2^${n}x2^${n}"
    for (( i = 1; i <= 5; i++ ))
    do
        for (( j = i ; j <= 5; j++ ))
        do
        ./tp.sh -a strassenSeuil -e1 ./gen_matrix/ex_${n}.${i} -e2 ./gen_matrix/ex_${n}.${j} -t
        done
    done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'

    # Envois une erreur si le resultat est different
    for (( i = 1; i <= 5; i++ ))
    do
        for (( j = i ; j <= 5; j++ ))
        do
        diff -q <(./tp.sh -a conv -e1 ./gen_matrix/ex_${n}.${i} -e2 ./gen_matrix/ex_${n}.${j} -p) \
        <(./tp.sh -a strassen -e1 ./gen_matrix/ex_${n}.${i} -e2 ./gen_matrix/ex_${n}.${j} -p)
        diff -q <(./tp.sh -a strassen -e1 ./gen_matrix/ex_${n}.${i} -e2 ./gen_matrix/ex_${n}.${j} -p) \
        <(./tp.sh -a strassenSeuil -e1 ./gen_matrix/ex_${n}.${i} -e2 ./gen_matrix/ex_${n}.${j} -p)
        done
    done
done
