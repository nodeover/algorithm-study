import time
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1

        def is_avail(t_day):
            bouquets = 0
            blooms = 0
            for b_day in bloomDay:
                if t_day >= b_day:  # 꽃이 자랄 시간이면
                    blooms += 1
                else:
                    blooms = 0
                if blooms >= k:
                    if bouquets + 1 >= m:
                        return True
                    bouquets += 1
                    blooms = 0
            return False

        min_day = min(bloomDay)
        max_day = max(bloomDay)

        # 이진탐색
        while min_day < max_day:
            mid_day = (min_day + max_day) // 2
            if is_avail(mid_day):
                max_day = mid_day
            else:
                min_day = mid_day + 1

        return min_day


s_time = time.time()
s = Solution()
bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
print(s.minDays(bloomDay, m, k))
print(time.time() - s_time)

s_time = time.time()
bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 2
print(s.minDays(bloomDay, m, k))
print(time.time() - s_time)

s_time = time.time()
bloomDay = [7, 7, 7, 7, 12, 7, 7]
m = 2
k = 3
print(s.minDays(bloomDay, m, k))
print(time.time() - s_time)

s_time = time.time()
bloomDay = eval(input())
m = int(input())
k = int(input())
print(s.minDays(bloomDay, m, k))
print(time.time() - s_time)
