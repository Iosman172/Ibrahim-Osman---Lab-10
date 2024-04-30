#!/bin/bash

import sys

# This input_line variable takes the number of shifts we want.
# The [1] means we take in 1 value
input_line=sys.argv[1]

new=""
counter=0

for line in sys.stdin:
    line = line.upper()

# We loop over every character in the string and concatenate the shifted
# value to the string 'new'.
    for char in line:
        if char.isalpha():
            if counter==5:
                counter=0
                new+=" "
            ascii_value = ord(char) + int(input_line)
            if ascii_value > ord("Z"):
                ascii_value-=26
            new+=chr(ascii_value)
            counter+=1
    print(new)
    new=""
    counter=0
