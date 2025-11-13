# 给你一个整数数组coins，表示不同面额的硬币；以及一个整数amount，表示总金额。
# 计算并返回可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回-1.
# 你可以认为每种硬币的数量是无限的。

# 完全背包的变形
# 完全背包公式：dfs(i,c) = max(dfs(i-1,c), dfs(i, c-w[i])+v[i])
# 这都题求最小，所以公式：dfs(i,c) = min(dfs(i-1,c), dfs(i, c-w[i])+1)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @cache
        def dfs(i, c):
            if i < 0:
                # 0表示合法，inf表示不合法，因为后面要求min
                return 0 if c == 0 else inf
            if c < coin[i]:
                return dfs(i-1, c)
            return min(dfs(i-1, c), dfs(i, c-coins[i])+1)、
        ans = dfs(n-1, amount)
        return ans if ans < inf else -1

    # 改成递推
    # f[i+1, c] = min(f[i,c], f[i+1, c-w[i]+1)
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [[inf] * (amount+1) for _ in range(n+1)]
        f[0][0] = 0
        for i, x in enumerate(coins):
            for c in range(amount+1):
                if c < x:
                    f[i+1][c] = f[i][c]
                else:
                f[i+1][c] = min(f[i][c], f[i+1][c-x+1])
        ans = f[n][amount]
        return ans if ans < inf else -1

    # 空间优化
    # 跟0-1背包一样，可以i和i+2全部模2，然后去掉i，正序计算就行，因为取最小值的时候不会改变f[i+1]的结果
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [inf] * (amount+1)
        f[0] = 0
        for x in coins:
            for c in range(x, amount+1):
                f[c] = min(f[c], f[c-x+1])
        ans = f[amount]
        return ans if ans < inf else -1        
                