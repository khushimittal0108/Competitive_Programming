#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    s=list(s)
    t=list(set(s))
    l1=[]
    for i in t:
        n=s.count(i)
        l=[n,i]
        l1.append(l)
    l1=sorted(sorted(l1,key=lambda x:x[1]),key=lambda x:x[0],reverse=True)
    for i in range(0,3):
        print(l1[i][1]+' '+str(l1[i][0]))
