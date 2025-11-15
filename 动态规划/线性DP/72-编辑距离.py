# 给你两个单词word1和word2，请返回将word1转换成word2所使用的最少操作数。
# 你可以对一个单词进行如下三种操作：
# ·插入一个字符
# ·删除一个字符
# ·替换一个字符

# 思路
# s = horse word1
# t = ros word2
# ·插入一个字符，相当于去掉t[j]
# ·删除一个字符，相当于去掉s[i]
# ·替换一个字符，相当于去掉s[i]和t[j]
# 在s[i] == t[j]的时候，都去掉就好，就可以得到跟最长公共子序列有一点类似的公式
# 最终：dfs(i,j) = 
#   dfs(i-1,j-1)                                    s[i]=t[j]
#   min(dfs(i,j-1), dfs(i-1,j), dfs(i-1,j-1)) + 1   s[i]!=t[j]
from cmath import inf
from functools import cache


class Solution:
    def minDistance1(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        @cache
        def dfs(i, j):
            if i < 0:
                return j+1
            if j < 0:
                return i+1
            if s[i] == t[j]:
                return dfs(i-1, j-1)
            return min(dfs(i, j-1), dfs(i-1,j),dfs(i-1,j-1)) + 1
        return dfs(n-1, m-1)

    # 递推
    # f[i+1][j+1] = 
    #   f[i][j]                                 s[i]=t[j]
    #   min(f[i+1][j], f[i][j+1], f[i][j]) + 1  s[i]!=t[j]
    def minDistance2(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        f = [[inf]*(m+1) for _ in range(n+1)]
        f[0] = list(range(m+1))
        for i, x in enumerate(s):
            f[i+1][0] = i+1
            for j, y in enumerate(t):
                if x == y:
                    f[i+1][j+1] = f[i][j]
                else:
                    f[i+1][j+1] = min(f[i+1][j], f[i][j+1], f[i][j]) + 1
        return f[n][m] # type: ignore
    
    # 空间优化，两个数组
    def minDistance3(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [list(range(m + 1)), [0] * (n + 1)]
        for i, x in enumerate(s):
            f[(i + 1) % 2][0] = i + 1
            for j, y in enumerate(t):
                f[(i + 1) % 2][j + 1] = f[i % 2][j] if x == y else \
                        min(f[i % 2][j + 1], f[(i + 1) % 2][j], f[i % 2][j]) + 1
        return f[n % 2][m]

    # 一个数组
    def minDistance(self, s: str, t: str) -> int:
        f = list(range(len(t) + 1))
        for x in s:
            pre = f[0]
            f[0] += 1  # f[0] = i + 1
            for j, y in enumerate(t):
                tmp = f[j + 1]
                f[j + 1] = pre if x == y else min(f[j + 1], f[j], pre) + 1
                pre = tmp
        return f[-1]
