#!/bin/python3

import math
import os
import random
import re
import sys
import string
# Complete the solve function below.
def solve(s):
    return string.capwords(s,' ')
#----------------------------------------------------------------------------------------- 
    # a_string = input().split(' ')
    # print(' '.join((word.capitalize() for word in a_string)))
#----------------------------------------------------------------------------------------- 
    
    # for i in s.split():
    #     print(i.capitalize(),end=' ')
#----------------------------------------------------------------------------------------- 
    
    # for i in s.split():
    #     s = s.replace(i,i.capitalize())
    # return s
#----------------------------------------------------------------------------------------- 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
