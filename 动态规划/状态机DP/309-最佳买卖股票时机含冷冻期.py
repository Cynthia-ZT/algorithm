# 给定一个整数数组prices，其中第prices[i]表示第i天的股票价格。
# 设计一个算法计算出最大利润。在满足一下约束条件下，你可以尽可能地完成更多的交易(多次买卖一只股票)：
# 卖出股票后，你无法在第二天买入股票(即冷冻期为1天)。
# 注意：你不能同时参与多笔交易(你必须在再次购买前出售掉之前的股票)。


from functools import cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, hold) -> int:
            if i < 0:
                if hold:
                    return -inf # type: ignore
                return 0
            
            if hold:
                # 就是今天买入股票，必须用前两天卖出的钱
                return max(dfs(i-1, True), dfs(i-2,False) - prices[i])
            return max(dfs(i-1, False), dfs(i-1, True) + prices[i])
        return dfs(n-1, 0)