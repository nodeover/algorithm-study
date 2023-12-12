import sys
s = sys.stdin.readline
q = int(s())
u = [s() for _ in range(q)]
r = []
i = 0
while 1:
    z = [int(v) for v in s().split()]
    if not z:
        break
    r.append(z)
    i += 1
ww = i/2
k = [-1]*i
m = [0]*q
n = [[] for _ in range(q)]
rmn = list(range(q))
o = list(range(i))
while 1:
    for i in o:
        k[i] += 1
        z = r[i]
        for c in range(k[i], q):
            to = z[k[i]] - 1
            if to in rmn:
                m[to] += 1
                n[to].append(i)
                break
            k[i] += 1
    max_v = max(m)
    if max_v > ww:
        print(u[m.index(max_v)].strip())
        break
    min_v = 1001
    p = []
    for i, v in enumerate(m):
        if v != -1 and v < min_v:
            min_v = v
            p = [i]
        elif v == min_v:
            p.append(i)
    if min_v == max_v:
        print(*[u[i].strip() for i in rmn], sep='\n')
        break
    o = []
    for i in p:
        rmn.pop(rmn.index(i))
        u[i] = None
        if n[i]:
            o.extend(n[i])
        m[i] = -1
        n[i] = None
