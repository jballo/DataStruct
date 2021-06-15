#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzbuzz' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def fizzbuzz(nums):
    # Write your code here
    for x in nums:
        printOut = ''
        if x % 3 == 0 and x % 5 == 0:
            printOut+='fizzbuzz'
        elif x % 3 == 0:
            printOut+='fizz'
        elif x% 5 == 0:
            printOut+='buzz'
        else:
            printOut+=str(x)
        print(printOut)
if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    fizzbuzz(arr)
