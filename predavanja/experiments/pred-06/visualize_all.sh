#! /bin/bash -eu

RESULTS=../pred-05/prosti-brojevi/*.csv

for filename in $RESULTS; do
  echo $filename
  poetry run python visualize.py $filename
done
