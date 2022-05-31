import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
vow = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())
li = sorted(list(input().split()))


def pick(n, toPick, picked):
    if toPick == 0:
        numVow = 0
        for i in vow:
            if i in picked:
                numVow += 1
        if l - numVow >= 2 and numVow >= 1:
            for i in picked:
                print(i, end='')
            print()
        return

    for i in range(n, c):
        picked.append(li[i])
        pick(i + 1, toPick - 1, picked)
        picked.pop(-1)


pick(0, l, [])
