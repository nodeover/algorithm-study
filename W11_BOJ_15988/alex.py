import sys
input = sys.stdin.readline

cnts = [0, 1, 2, 4, 7]
for _ in range(int(input())):
    n = int(input())
    for i in range(len(cnts) - 1, n + 1):
        cnts.append((cnts[-3] + cnts[-2] + cnts[-1]) % 1000000009)
    print(cnts[n])
