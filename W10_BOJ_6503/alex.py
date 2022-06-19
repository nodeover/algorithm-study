from collections import defaultdict

while True:
    m = int(input())
    if m == 0:
        break
    s = input()
    hd = defaultdict(int)

    left, right = -1, -1
    max_cnt = 0
    while left <= right and right < len(s) - 1:
        cnt = len(hd)
        if cnt < m or (cnt == m and hd[s[right + 1]] > 0):
            right += 1
            hd[s[right]] += 1
        else:
            left += 1
            hd[s[left]] -= 1
            if hd[s[left]] == 0:
                del hd[s[left]]
        max_cnt = max(right - left, max_cnt)

    print(max_cnt)
