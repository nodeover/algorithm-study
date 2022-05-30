from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        orders = [0] * numCourses
        for a, b in prerequisites:
            orders[a] += 1

        st = []
        res = []

        for i in range(numCourses):
            if not orders[i]:
                st.append(i)

        for i in range(numCourses):
            if not len(st):
                return []

            res.append(st.pop(0))

            for pre in prerequisites:
                if pre[1] == res[i]:
                    orders[pre[0]] -= 1
                    if not orders[pre[0]]:
                        st.append(pre[0])

        return res
