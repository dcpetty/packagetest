#!/bin/env sh
  echo ''; cd src; \
python3 foo.py "foo bar"; \
  echo ''; \
python3 packagetest "foo bar"; \
  echo ''; \
python3 -m packagetest "foo bar"; \
  echo ''; cd  ..; \
