import os
import sys
#
# Complete the simpleArraySum function below.
#
def compareTriplets(a, b):
    #
    # Write your code here.
    #
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1

    return alice, bob

if __name__ == '__main__':

    a = [1, 2, 3]
    b = [4, 10, 11]
    result = compareTriplets(a, b)
    print(str(result) + '\n')
