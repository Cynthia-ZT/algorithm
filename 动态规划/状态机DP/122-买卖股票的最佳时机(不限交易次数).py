# 给你一个整数数组prices，其中prices[i]表示某只股票第i天的价格。
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候最多只能持有一股股票。你也可以先购买，然后在同一天出售。

# 启发思路：最后一天发生了什么
# 从第0天开始到第5天结束时的利润 = 从第0天开始到第4天结束时的利润 + 第5天的利润
#   第5天的利润：什么也不做 or 买入股票 or 卖出股票
#
# 关键词：天数，是否持有股票
# 子问题？到第i天结束时，持有/未持有股票的最大利润
# 当前操作？下面的情况可以用转换图表示，这种表示状态之间转换关系的图就是状态机
#   未持有股票：什么也不做 or 买入
#   持有股票：什么也不做 or 卖出
# 下一个子问题？到第i-1天结束时，持有/未持有股票的最大利润
# 
# 定义dfs(i,0)表示第i天结束时，未持有股票的最大利润
# 定义dfs(i,1)表示第i天结束时，持有股票的最大利润
#
# 由于第i-1天的结束就是第i天的开始
# dfs(i-1,·)也表示第i天开始时的最大利润
# 得出：
# 第i天结束时
# 一开始未持有股票：
#   什么也不做，dfs(i,0) = dfs(i-1,0)
#   买入股票，dfs(i,1) = dfs(i-1,0) - price[i] 注：第i-1天的状态就是第i天的开始状态
# 一开始持有股票：
#   什么也不做，dfs(i,1) = dfs(i-1,1)
#   卖出股票，dfs(i,0) = dfs(i-1,1) + price[i]
# 最后
# dfs(i,0) = max(dfs(i-1,0), dfs(i-1,1) + price[i])
# dfs(i,1) = max(dfs(i-1,1), dfs(i-1,0) - price[i])
# 递归边界
# dfs(-1,0) = 0 表示第0天开始未持有股票，利润为0
# dfs(-1,1) = -inf，第0天开始不可能持有股票
# 递归入口：因为最后一天股票不卖出去不会比卖出去利润大
# max(dfs(n-1, 0), dfs(n-1, 1)) = dfs(n-1,0)

from cmath import inf
from functools import cache
from typing import List


class Solution:
    # 时间复杂度：O(n)，空间复杂度O(n)
    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, hold) -> int:
            if i < 0:
                if hold:
                    return -inf # type: ignore
                return 0
            
            if hold:
                return max(dfs(i-1, True), dfs(i-1,False) - prices[i])
            return max(dfs(i-1, False), dfs(i-1, True) + prices[i])
        return dfs(n-1, 0)

    # 改递推
    # f[i][0] = max(f[i-1][0], f[i-1][1]+prices[i])
    # f[i][1] = max(f[i-1][1], f[i-1][0]-prices[i])
    # i+1:
    # f[0][0] = 0
    # f[0][1] = -inf
    # f[i+1[0] = max(f[i][0], f[i][1]+prices[i])
    # f[i+1][1] = max(f[i][1], f[i][0]-prices[i])
    # 答案f[n,0]
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[0]*2 for _ in range(n+1)]
        f[0][1] = -inf # type: ignore
        for i, x in enumerate(prices):
            f[i+1][0] = max(f[i][0], f[i][1]+prices[i])
            f[i+1][1] = max(f[i][1], f[i][0]-prices[i])
        return f[n][0]

    # # 时间复杂度：O(n)，空间复杂度O(1)
    def maxProfit(self, prices: List[int]) -> int:
        f0 = 0
        f1 = -inf
        for x in prices:
            new_f0 = max(f0, f1+x)
            f1 = max(f1, f0-x)
            f0 = new_f0
        return f0 # type: ignore