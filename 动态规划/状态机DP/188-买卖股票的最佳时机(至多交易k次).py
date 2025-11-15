# 给定一个整数数组prices，它的第i个元素prices[i]是一只给定的股票在第i天的价格
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成k笔交易。
# 注意：你不能同时参与多笔交易(你必须在再次购买前出售掉之前的股票)。

# 思路
# 定义dfs(i,j,0)，表示到第i天结束时完成至多j笔交易，未持有股票的最大利润
# 定义dfs(i,j,1)，表示到第i天结束时完成至多j笔交易，持有股票的最大利润
# 第i天开始未持有
#   什么都不干: dfs(i,j,0)=dfs(i-1,j,0)
#   买入：dfs(i,j,1)=dfs(i-1,j-1,0)-prices[i]
# 第i天开始持有
#   什么都不干：dfs(i,j,1)=dfs(i-1,j,1)
#   卖出：dfs(i,j,0)=dfs(i-1,j,1)+prices[i]
# 注：这里把买入算成一次交易，也可以把卖出算成一次交易
# 递归边界：
# dfs(·,-1,·) = -inf，没有交易次数了，不合法
# dfs(-1,j,0) = 0，第0天开始未持有股票，利润0
# dfs(-1,j,1) = -inf，第0天开始持有股票，不合法
# 递归入口：
# max(dfs(n-1,k,0),dfs(n-1,k,1)) = dfs(n-1,k,0)

from cmath import inf
from functools import cache
from typing import List


class Solution:
    # 时间复杂度O(n*k)，空间复杂度(n*k)
    def maxProfit1(self, k: int,prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, j, hold) -> int:
            if j < 0:
                return -inf # type: ignore
            if i < 0:
                if hold:
                    return -inf # type: ignore
                return 0
            
            if hold:
                return max(dfs(i-1, j,True), dfs(i-1, j-1, False) - prices[i])
            return max(dfs(i-1, j, False), dfs(i-1, j,True) + prices[i])
        return dfs(n-1, k, 0)
    # 改递推
    # f[i][j][0] = max(f[i-1][j][0], f[i-1][j][1]+prices[i])
    # f[i][j][1] = max(f[i-1][j][1], f[i-1][j-1][0]-prices[i])
    # 最终
    # f[0][j][0] = 0        j >= 1
    # f[0][j][1] = -inf     j >= 1
    # f[·][0][·] = -inf
    # f[i+1][j][0] = max(f[i][j][0], f[i][j][1]+prices[i])
    # f[i+1][j][1] = max(f[i][j][1], f[i][j-1][0]-prices[i])
    # 注：这里没有把j+1因为代码中的j是从1开始的
    def maxProfit2(self, k: int,prices: List[int]) -> int:
        n = len(prices)
        f = [[[-inf] * 2 for _ in range(k+2)] for _ in range(n+1)]
        for j in range(1, k+2):
            f[0][j][0] = 0
        for i, x in enumerate(prices):
            for j in range(1, k+2):
                f[i+1][j][0] = max(f[i][j][0], f[i][j][1]+x)
                f[i+1][j][1] = max(f[i][j][1], f[i][j-1][0]-x)
        return f[n][k+1][0] # type: ignore

    # 去掉f[i]维度优化空间到O(k)
    def maxProfit(self, k: int,prices: List[int]) -> int:
        n = len(prices)
        f = [[-inf] * 2 for _ in range(k+2)]
        for j in range(1, k+2):
            f[j][0] = 0
        for i, x in enumerate(prices):
            for j in range(k+1, 0, -1):
                f[j][1] = max(f[j][1], f[j-1][0]-x)
                f[j][0] = max(f[j][0], f[j][1]+x)
        return f[k+1][0] # type: ignore
    
    # 恰好k次
    # f[0][1][0]=0，其余-inf
    # 注意前面塞了一个状态，f[0][1]才是恰好完成0次的状态

    # 至少k次
    # f[i][-1][·]等价于f[i][0][·]
    # 所以每个f[i]的最前面不需要插入状态
    # [至少0次]等价于[可以无限次交易]
    # 所以f[i][0][·]就是无限次交易下的最大利润，转移方程一样
    # f[0][0][0] = 0, 其余-inf
    # f[i+1[0][0] = max(f[i][0][0], f[i][0][1]+prices[i])
    # f[i+1][0][1] = max(f[i][0][1], f[i][0][0]-prices[i])