#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    # Start at 0 (sea level)
    level = 0

    # Initialize valley count at 0
    valleys = 0

    # We can find out the number of valleys by finding out the number of times he
    # comes back up to sea level. 
    for x in s:
        if x == 'U' and level == -1:
            level += 1
            valleys += 1
        elif x == 'U':
            level += 1
        else:
            level -= 1
        
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
