class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        # base condition
        if len(bloomDay) < m * k:
            return -1

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2
            found = m
            flowers = 0

            for flower in bloomDay:
                if flower <= mid:
                    flowers += 1
                else:
                    flowers = 0

                if flowers == k:
                    found -= 1
                    flowers = 0

            if found <= 0:
                right = mid
            else:
                left = mid + 1

        return left
