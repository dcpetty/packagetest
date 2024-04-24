#!/bin/env bash

tests=(
  'python3 qux.py'
  'python3 alternative'
  'python3 -m alternative'
)

cd ./src
for c in "${tests[@]}"; do
  echo "# $c"
  sh -c "$c"
  echo ""
done
