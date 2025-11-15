# 给你一个字符串s，找出其中最长的回文子序列，并返回该序列的长度。
# 子序列的定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列

# 思路
# s = eacbba
# 方法1
# [转换]求s和反转后s的LCS(最长公共子序列)

# 方法2
# [选或不选]从两侧向内缩小问题规模
# 最后一位和第一位如果不等，只能选一个
# 最后一位和第一位如果相等，都选
# 公式类似LCS
# 定义dfs(i,j)表示s[i]到s[j]的最长回文子序列的长度
# dfs(i,j)=
#   dfs(i+1,j-1)+2              s[i]==s[j]
#   max(dfs(i+1,j),dfs(i,j-1))  s[i]!=s[j]
# 递归边界
# dfs(i,i) = 1
# dfs(i+1,i) = 0
# 比如遇到bb时，会从dfs(i,i+1)递归到dfs(i+1,i)
# 递归入口
# dfs(0, n-1)

from functools import cache


class Solution:
    # 时间复杂度：O(n^2)，空间复杂度O(n^2)
    def longestPalindromeSubseq1(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i, j):
            if i==j:
                return 1
            if i > j:
                return 0
            if s[i] == s[j]:
                return dfs(i+1,j-1) + 2
            return max(dfs(i+1,j), dfs(i,j-1))
        return dfs(0, n-1) 
    
    # 递推
    # f[i][j] = f[i+1][j-1] +2                s[i]==s[j]
    # f[i][j] = max(f[i+1][j],f[i][j-1])      s[i]!=s[j]
    # 因为需要从i+1转移到i，所以i要倒序枚举
    # 因为需要从j-1转移到j，所以j要正序枚举
    # 入口：f[0][n-1]
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        f = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            f[i][i] = 1
            for j in range(i+1,n):
                if s[i] == s[j]:
                    f[i][j] = f[i+1][j-1]+2
                else:
                    f[i][j] = max(f[i+1][j], f[i][j-1])
        return f[0][n-1]