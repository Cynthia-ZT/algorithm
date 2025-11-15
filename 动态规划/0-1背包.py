# 有n个物品，第i个物品的体积为w[i]，价值v[i]，每个物品至多选一个，求体积和不超过capacity时的最大价值和

# 回溯三问
# 当前操作？枚举第i个物品选或不选
#   不选，剩余容量不变；
#   选，剩余容量减少w[i]
# 子问题？在剩余容量是c时，从前i个物品中得到的最大价值和
# 下一个子问题？分类讨论：
#   不选：剩余容量为c时，从前i-1个物品中得到的最大价值和
#   选：在剩余容量为c-w[i]时，从前i-1个物品得到的最大价值和
# dfs(i,c) = max(dfs(i-1, c), dfs(i-1, c-w[i])+v[i])

from functools import cache
from typing import List


def zero_one_knapsack(capacity: int, w: List[int], v: List[int]) -> int:
    n = len(w)
    @cache
    def dfs(i, c):
        if i < 0:
            return 0
        if c < w[i]:
            return dfs(i-1, c)
        return max(dfs(i-1, c), dfs(i-1, c-w[i])+v[i])
    return dfs(n-1, capacity)