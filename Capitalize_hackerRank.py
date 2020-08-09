#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    flag=0
    S=""
    for i in s:
        if flag==0:
            S=S+i.upper()
        else:
            S=S+i
        if i ==" ":
            flag=0
        else:
            flag=1
    return S

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
