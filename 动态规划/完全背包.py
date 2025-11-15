# 有n种物品，第i种物品的体积为w[i]，价值为v[i]
# 每种物品无限次重复选，求体积和不超过capacity时的最大价值和

# 回溯三问
# 当前操作？
#   不选，剩余容量不变；选，剩余容量减少w[i]
# 子问题？
#   在剩余容量为c时，从前i种物品中得到的最大价值和
# 下一个子问题？分类讨论
#   不选：在剩余容量为c时，从前i-1种物品中得到的最大价值和
#   选一个：在剩余容量为c-w[i]时，从前i种物品中得到的最大价值和

# dfs(i,c) = max(dfs(i-1,c), dfs(i, c-w[i])+v[i])

from functools import cache
from typing import List


def unbound_knapsack(capacity: int, w: List[int], v: List[int]) -> int:
    n = len(w)
    @cache
    def dfs(i, c):
        if i < 0:
            return 0
        if c < w[i]:
            return dfs(i-1, c)
        return max(dfs(i-1, c), dfs(i, c-w[i])+v[i])
    return dfs(n-1, capacity)