#!/bin/bash

echo "Multiplication conventionnelle"
for i in {1..5}
do
    for j in {i..5}
    do
    ./tp.sh -a conv -e1 ./gen_matrix/ex_1.${i} -e2 ./gen_matrix/ex_1.${j} $@
    done
done