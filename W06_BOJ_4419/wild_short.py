import sys
s = sys.stdin.readline

q = int(s())
u = [s() for _ in range(q)]

r = dict()
i = 0
while 1:
    z = [int(v) for v in s().split()]
    if not z:
        break
    r[i] = z
    i += 1
ww = i/2
k = [0]*i

m = [0]*q
n = [[] for _ in range(q)]

rmn = list(range(q))
o = r.keys()
while 1:
    for i in o:
        z = r[i]
        to = z[k[i]] - 1
        if to not in rmn:
            for _ in range(k[i], q):
                k[i] += 1
                to = z[k[i]] - 1
                if to in rmn:
                    break
        if n[to] is not None:
            m[to] += 1
            n[to].append(i)
    max_v = max(m)
    if max_v > ww:
        w = [m.index(max_v)]
        break
    min_v = 1001
    p = []
    for i, v in enumerate(m):
        if v != -1:
            if v < min_v:
                min_v = v
                p = [i]
            elif v == min_v:
                p.append(i)
    if min_v == max_v:
        w = rmn
        break
    for i in p:
        rmn.pop(rmn.index(i))

    o = []
    for i in p:
        if n[i]:
            o.extend(n[i])
        m[i] = -1
        n[i] = None
    for i in o:
        k[i] += 1

for i in w:
    print(u[i].strip())
