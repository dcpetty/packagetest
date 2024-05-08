#!/bin/env bash

tests=(
  'python3 src/main.py "foo bar"'
  'python3 src/mod "foo bar"'
  'python3 -m src.mod "foo bar"'
  'python3 src/run.py "foo bar"'
  'python3 src/tests "foo bar"'
  'python3 -m src.tests "foo bar"'
)

for c in "${tests[@]}"; do
  python3 -c "print(f' $c '.center(72, '#'))"
  sh -c "$c"
  echo ""
done

tests=(
  'python3 main.py "foo bar"'
  'python3 mod "foo bar"'
  'python3 -m mod "foo bar"'
  'python3 run.py "foo bar"'
  'python3 tests "foo bar"'
  'python3 -m tests "foo bar"'
)

cd ./src
for c in "${tests[@]}"; do
  python3 -c "print(f' $c '.center(72, '#'))"
  sh -c "$c"
  echo ""
done
