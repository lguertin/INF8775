#!/bin/bash

for n in {1000 3000 10000 30000 100000 300000 1000000 3000000 6000000 8000000}
do
    echo "Glouton"
    for (( i = 1; i <= 10; i++ ))
    do
        ./tp.sh -a glouton -e ./exemplaires/ex_${n}.${i} -t
    done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'

    echo "Dynamique"
    for (( i = 1; i <= 10; i++ ))
    do
        ./tp.sh -a dp -e ./exemplaires/ex_${n}.${i} -t
    done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'

    echo "Heuristique"
    for (( i = 1; i <= 10; i++ ))
    do
        ./tp.sh -a heuristique -e ./exemplaires/ex_${n}.${i} -t
    done | xargs -n1 | awk '{sum+=$0}END{print sum/NR}'
done
