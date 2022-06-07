import sys

input = sys.stdin.readline


def solve(n, s):
    start, end, cnt, res = 0, 0, 0, 0
    l = len(s)
    check = [0] * 128

    while start <= end:
        if cnt < n or (cnt == n and check[ord(s[end + 1])] > 0):
            end += 1
            check[ord(s[end])] += 1
            if check[ord(s[end])] == 1:
                cnt += 1
        else:
            start += 1
            check[ord(s[start])] -= 1
            if check[ord(s[start])] == 0:
                cnt -= 1
        res = max(end - start, res)
        if end == l - 1:
            break

    return res


while True:
    n = int(input())
    if not n:
        break
    print(solve(n, input()))