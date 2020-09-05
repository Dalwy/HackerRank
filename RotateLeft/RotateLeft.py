def rotLeft(a, d):
    return a[d:] + a[:d]

if __name__ == '__main__':
    contests = []
    nk = input().split()
    n = int(nk[0])
    d = int(nk[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    print(' '.join(map(str, result)))
