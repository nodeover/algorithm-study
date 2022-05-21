# comb 구현코드
l, c = map(int, input().split())
j = ['a', 'e', 'i', 'o', 'u']
cl = input().split()
cl.sort()


def comb(arr, length):
    res = []
    if length > len(arr):
        return res
    if length ==1:
        for i in arr:
            res.append([i])
    elif length>1:
        for i in range(len(arr) - length+1):
            for j in comb(arr[i+1:],length-1):
                res.append([arr[i]] + j)
    return res

for s in comb(cl, l):
    cnt = 0
    for a in j:
        if a in s:
            cnt += 1

    if cnt and l - cnt >= 2:
        print(''.join(s))
