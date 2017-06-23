#!/bin/bash


FILES=../src/*.py
for f in $FILES
do 
    echo "Testing file $f"
    python3 $f
done
