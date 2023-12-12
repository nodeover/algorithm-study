import sys
s = sys.stdin.readline

q = int(s())
u = [s() for i in range(q)]

r = dict()
i = 0
while 1:
    z = [int(v) for v in s().split()]
    if not z:
        break
    r[i] = z
    i += 1
j = len(r)
k = [0 for _ in range(j)]

m = [0 for j in range(q)]
n = [set() for j in range(q)]

rmn = [i for i in range(q)]
o = range(j)
while 1:
    for i in o:
        z = r[i]
        to = z[k[i]] - 1
        if to not in rmn:
            for _ in range(k[i], len(z)):
                k[i] += 1
                to = z[k[i]] - 1
                if to in rmn:
                    break
        if n[to] is not None:
            m[to] += 1
            n[to].add(i)
    max_v = max(m)
    if max_v > j/2:
        w = [m.index(max_v)]
        break
    min_v = 1001
    p = []
    for v, i in zip(m, range(q)):
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

    o = set()
    for i in p:
        if n[i]:
            o = o.union(n[i])
        m[i] = -1
        n[i] = None
    for i in o:
        k[i] += 1

for i in w:
    print(u[i].strip())
