from typing import List


class Solution:
    def solve(self, mat: List[List[str]]) -> None:
        r = len(mat)
        c = len(mat[0])

        def dfs(i, j):
            if i < 0 or j < 0 or j > c - 1 or i > r - 1:
                return
            mat[i][j] = 'T'
            if i + 1 < r:
                if mat[i + 1][j] == 'O':
                    dfs(i + 1, j)
            if i - 1 >= 0:
                if mat[i - 1][j] == 'O':
                    dfs(i - 1, j)
            if j + 1 < c:
                if mat[i][j + 1] == 'O':
                    dfs(i, j + 1)
            if j - 1 >= 0:
                if mat[i][j - 1] == 'O':
                    dfs(i, j - 1)

        for i in range(r):
            for j in range(c):
                if j == 0 or j == c - 1:
                    if mat[i][j] == 'O':
                        dfs(i, j)
                if i == 0 or i == r - 1:
                    if mat[i][j] == 'O':
                        dfs(i, j)
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 'O':
                    mat[i][j] = 'X'
                if mat[i][j] == 'T':
                    mat[i][j] = 'O'
