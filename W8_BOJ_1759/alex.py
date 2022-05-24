# combination 사용 코드

from itertools import combinations

l, c = map(int, input().split())
j = ['a','e','i','o','u']
cl = input().split()
cl.sort()

for s in combinations(cl,l):
    cnt = 0
    for a in j:
        if a in s:
            cnt+=1

    if cnt and l-cnt>=2:
        print(''.join(s))