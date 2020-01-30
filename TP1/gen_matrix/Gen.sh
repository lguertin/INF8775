#!/bin/bash
for N in {1..10}; do
  for I in {1..5}; do
    ./Gen $N "ex_"$N"."$I
  done
done
