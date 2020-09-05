import os
import sys





def luckBalance(k, contests):
    print(contests.sort())
    luck = 0
    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        elif k > 0:
            luck+= contest[0]
            k -= 1
        else:
            luck -= contest[0]
    return luck


if __name__ == '__main__':
    contests = []
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)
    print(str(result) + '\n')
