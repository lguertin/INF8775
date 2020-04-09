#!/bin/bash

OPTIONS=""
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -k)
    PROPAGATION="$2"
    shift
    ;;
    -e)
    EX_PATH_1="$2"
    shift
    ;;
    -p)
    OPTIONS="${OPTIONS}${1} "
    ;;
    *)
        echo "Argument inconnu: ${1}"
        exit
    ;;
esac
shift
done

python3 ./main.py -e $EX_PATH_1 -k $PROPAGATION $OPTIONS
