#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2==0: 
        if n in range (2,5):
            print('Not weird')
        if n in range(6, 20):
            print('Weird')
        if n > 20:
            print('Not weird')
    else:
        print('Weird') 
