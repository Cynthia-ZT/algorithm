# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
# n皇后问题研究的是如何将n个皇后放置在nxn的棋盘上，并且使皇后彼此不能相互攻击。
# 给你一个整数n，返回所有不同n皇后问题的解决方案。
# 每一种解法包含一个不同的n皇后问题的棋子放置方案，该方案中'Q'和'.'分别代表了皇后和空位。

# 思路：
# 每行每列恰好有一个皇后
# 反证法：
# 不是每行一个又不能放两个，就假设有一行一个皇后都没有，那么n-1行要放n个皇后，必然有一行要放两个皇后，矛盾
# 用一个长为n的数组col记录皇后的位置
# 即第i行的皇后在第col[i]列
# 那么col必须是一个0到n-1的排列
# 如col==[1,3,0,2]或者[2,0,3,1]
# 和全排列一样，枚举col的所有排列
# 这样每行只选一个，每列只选一个
# 剩下要做的，就是判断右上和左上是否有其他皇后

# 用r表示行号，c表示列号
# 右上方向的皇后
# r+c是一个定值
# 假设要在(2,0)放皇后，那么之前不能有r+c=2的皇后
# 左上方向的皇后
# r-c是一个定值
# 假设要在(2,3)放皇后，那么之前不能有r-c=-1的皇后

from typing import List


class Solution:
    # 时间复杂度O(n2*n!)，空间复杂度O(n)
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = [] * n
        def valid(r, c):
            for R in range(r):
                C = col[R]
                if r+c == R+C or r-c == R-C:
                    return False
            return True

        def dfs(r, s):
            if r == n:
                ans.append(['.'*c + 'Q', '.'*(n-1-c) for c in col])
                return
            for c in s:
                if valid(r, c):
                    col[r] = c
                    dfs(r+1, s-{c})
        dfs(0, set(range(n)))
        return ans

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = [] * n
        on_path = [False] * n
        m = 2*n-1
        diag1 = [False] * m
        diag2 = [False] * m

        def dfs(r):
            if r == n:
                ans.append(['.'*c + 'Q', '.'*(n-1-c) for c in col])
                return
            for c in range(n):
                if not on_path[c] and not diag1[r+c] and not diag2[r-c]:
                    col[r] = c
                    on_path[c] = diag1[c] = diag[c] = True
                    dfs(r+1, s-{c})
                    on_path[c] = diag1[c] = diag[c] = False
        dfs(0)
        return ans