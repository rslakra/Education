#!/bin/bash
# Author: Rohtash Lakra
#
echo
#if [[ "$#" -eq 1 ]]; then # Specific Test
#  python -m unittest discover -s ./tests/ -p "$1"
#else # No Arguments Supplied
#  python -m unittest discover -s ./tests/ -p "test_*.py"
#fi
python -m unittest
# python -m unittest tests/core/adts/test_stack.py
echo