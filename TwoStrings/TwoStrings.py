
import math
import os
import random
import re
import sys
import json
def twoStrings(s1, s2):
    if set(s1) & set(s2):
        return 'YES'
    else:
        return 'NO'
if __name__ == '__main__':

    s1 = "hi"
    s2 = "World"
    result = twoStrings(s1, s2)
    print(result)

