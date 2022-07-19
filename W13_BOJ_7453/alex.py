import sys

input = sys.stdin.readline

n = int(input())
ab, cd = [], []

l = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        ab.append(l[i][0] + l[j][1])
        cd.append(l[i][2] + l[j][3])

ab.sort()
cd.sort()

ans = 0
p_ab, p_cd = 0, len(cd) - 1

while p_ab < len(cd) and p_cd >= 0:
    sum_val = ab[p_ab] + cd[p_cd]
    if sum_val == 0:
        f_ab, f_cd = 1, 1

        while p_ab + f_ab < len(cd) and ab[p_ab] == ab[p_ab + f_ab]:
            f_ab += 1

        while p_cd - f_cd >= 0 and cd[p_cd] == cd[p_cd - f_cd]:
            f_cd += 1

        ans += f_ab * f_cd
        p_ab += f_ab
        p_cd -= f_cd

    elif sum_val > 0:
        p_cd -= 1
    else:
        p_ab += 1

print(ans)
