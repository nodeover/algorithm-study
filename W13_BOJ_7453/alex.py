from collections import defaultdict

n = int(input())
A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

pair1 = defaultdict(int)
pair2 = defaultdict(int)
for a in A:
    for b in B:
        pair1[a + b] += 1

for c in C:
    for d in D:
        pair2[c + d] += 1

ans = 0
for pair in pair1.keys():
    if pair * -1 in pair2.keys():
        ans += pair1[pair]
print(ans)
