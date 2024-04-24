#!/bin/env bash

tests=(
  'python3 foo.py "foo bar"' 
  'python3 packagetest "foo bar"' 
  'python3 -m packagetest "foo bar"'
)

cd ./src
for c in "${tests[@]}"; do
  echo "# $c"
  sh -c "$c"
  echo ""
done
