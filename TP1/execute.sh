#!/bin/bash

n=4

echo "Multiplication conventionnelle ${n}x${n}"
for i in 1 2 3 4 5
do
    for j in 1 2 3 4 5
    do
    ./tp.sh -a conv -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -t
    done
done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'

echo "Multiplication diviser-pour-regner ${n}x${n}"
for i in 1 2 3 4 5
do
    for j in 1 2 3 4 5
    do
    ./tp.sh -a strassen -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -t
    done
done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'

echo "Multiplication diviser-pour-regner avec seuil ${n}x${n}"
for i in 1 2 3 4 5
do
    for j in 1 2 3 4 5
    do
    ./tp.sh -a strassenSeuil -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -t
    done
done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'

# Tests
for i in 1 2 3 4 5
do
    for j in 1 2 3 4 5
    do
    diff <(./tp.sh -a conv -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -p) \
    <(./tp.sh -a strassen -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -p)
    diff <(./tp.sh -a strassen -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -p) \
    <(./tp.sh -a strassenSeuil -e1 ./gen_matrix/ex_${n}.$i -e2 ./gen_matrix/ex_${n}.$j -p)
    done
done