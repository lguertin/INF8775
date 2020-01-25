#!/bin/bash

echo "Multiplication conventionnelle"
for i in 1 2 3 4 5
do
    for j in 1 2 3 4 5
    do
    ./tp.sh -a conv -e1 ./gen_matrix/ex_1.$i -e2 ./gen_matrix/ex_1.$j -t $@
    done
done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'

echo "Multiplication diviser-pour-regner"
for i in 1 2 3 4 5
do
    for j in 1 2 3 4 5
    do
    ./tp.sh -a strassen -e1 ./gen_matrix/ex_1.$i -e2 ./gen_matrix/ex_1.$j -t $@
    done
done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'

echo "Multiplication diviser-pour-regner avec seuil"
for i in 1 2 3 4 5
do
    for j in 1 2 3 4 5
    do
    ./tp.sh -a strassenSeuil -e1 ./gen_matrix/ex_1.$i -e2 ./gen_matrix/ex_1.$j -t $@
    done
done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'
