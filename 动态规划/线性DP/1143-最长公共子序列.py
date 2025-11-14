# 给定两个字符串text1和text2，返回这两个字符串的最长公共子序列的长度。如果不存在公共子序列，返回0.
# 一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符(也可以不删除任何字符)后组成的新字符串。
# 例如："ace"是"abcde"的子序列，但"aec"不是"abcde"的子序列。
# 两个字符串的公共子序列是这两个字符串所共同拥有的子序列。

# 子数组/子串 subarray/substring 是连续的
# 子序列 subsequence 不一定是连续的

# 启发思路：子序列本质上就是选或不选，考虑最后一对字母，分别叫x和y
#   不选x不选y
#   不选x选y
#   选x不选y
#   选x选y
# 一般化：
# 当前操作？考虑s[i]和t[j]选或不选
# 子问题？s的前i个字母和t的前j个字母的LCS长度
# 下一个子问题？
#   s的前i-1个字母和t的前j-1个字母的LCS长度
#   s的前i-1个字母和t的前j个字母的LCS长度
#   s的前i个字母和t的前j-1个字母的LCS长度
# dfs(i,j) = max(dfs(i-1,j), dfs(i,j-1),dfs(i-1,j-1)+1) s[i]=t[j]
# dfs(i,j) = max(dfs(i-1,j), dfs(i,j-1),dfs(i-1,j-1)) s[i]!=t[j]
# 所以dfs(i,j) = max(dfs(i-1,j), dfs(i,j-1),dfs(i-1,j-1)+(s[i]=t[j]))
# 不能忽略的问题，
#   s[i]=t[j]时，不需要考虑dfs(i-1,j)和dfs(i,j-1)，也就是只选一个
#   s[i]!=t[j]时，不需要考虑dfs(i-1,j-1)，也就是都选
# 最终：dfs(i,j) = 
#   dfs(i-1,j-1) + 1            s[i]=t[j]
#   max(dfs(i,j-1), dfs(i-1,j)) s[i]!=t[j]

class Solution:
    # 时间复杂度O(n*m)，空间复杂度O(n*m)
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            
            if s[i] == t[j]:
                return dfs(i-1, j-1)+1
            return max(dfs(i, j-1), dfs(i-1,j))
        return dfs(n-1, m-1)
    
    # 改递推
    # f[i+1][j+1] = 
    # s[i]==t[j]: f[i][j]+1
    # s[i]!=t[j]: max(f[i+1][j], f[i][j+1])
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        f = [[0]*(m+1) for _ in range(n+1)]

        for i, x in enumerate(s):
            for j, y in enumerate(t):
                if x == y:
                    f[(i + 1) % 2][j + 1] = f[i % 2][j] + 1 
                else:
                    max(f[i % 2][j + 1], f[(i + 1) % 2][j])
        return f[n % 2][m]

    # 优化空间复杂度为O(m)
    # 正序计算会覆盖掉，下面用记录的方法解决了
    # 问：为什么 j 不能倒序循环？
    # 答：本题 f[i+1][j+1] 需要从 f[i+1][j] 转移过来，这只能正序枚举 j。倒序枚举的话，f[i+1][j] 还没有计算出来。

    def longestCommonSubsequence(self, s: str, t: str) -> int:
        f = [0] * (len(t) + 1)
        for x in s:
            pre = f[0]  # 0
            for j, y in enumerate(t):
                tmp = f[j + 1]
                if x == y:
                    f[j + 1] = pre + 1  
                else:
                     max(f[j + 1], f[j])
                pre = tmp
        return f[-1]
