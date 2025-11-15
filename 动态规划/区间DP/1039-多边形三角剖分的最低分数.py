# 你有一个凸的n变形，其每个定点都有一个整数值。给定一个整数数组values，其中values[i]是第i个定点的值(即顺时针顺序)
# 假设将多边形部分剖分为n-2个三角形。对于每个三角形，该三角形的值是顶点标记的乘积，三角剖分的分数是进行三角剖分后所有n-2个三角形的值之和。
# 返回多边形进行三角剖分后可以得到的最低分。

# 思路
# 看多变形的一条边，最终会是哪些三角形的边呢？就可以枚举另外一个定点来得到三角形
# 具体来说
# 数组values简计为v
# 定义[从i到j]表示沿着边从顶点i顺时针到顶点j，在加上直接从j到i的这条边所组成的多边形
# 子问题：计算从i到j的最低得分，枚举k
# 下一个子问题：
#   计算i到k的最低得分
#   计算k到j的最低得分
# 定义dfs(i,j)表示从i到j这个多边形的最低得分
# dfs(i,j) = min(dfs(i,k)+dfs(k,j)+v[i]*v[j]*v[k]) k从i+1到j-1
# 递归边界 dfs(i,i+1) = 0
# 递归入口 dfs(0, n-1)

from cmath import inf
from functools import cache
from typing import List


class Solution:
    # 时间复杂度：O(n^3)，空间复杂度(n^2)
    def minScoreTriangulation1(self, v: List[int]) -> int:
        n = len(v)

        @cache
        def dfs(i,j):
            if j == i+1:
                return 0
            res = inf
            for k in range(i+1, j):
                res = min(res, dfs(i,k) + dfs(k,j) + v[i]*v[j]*v[k]) # type: ignore

        return dfs(0, n-1) # type: ignore
    
    # 递推
    # f[i][j] = min(f[i][k]+f[k][j]+v[i]*v[j]v[k]) k从i+1到j-1
    # i < k，f[i]要从f[k]转移过来，所以要倒序枚举
    # j > k, f[i][j]要从f[i][k]转移过来，所以要正序枚举
    # 答案f[0][n-1] 
    def minScoreTriangulation(self, v: List[int]) -> int:
        n = len(v)
        f = [[0]*n for _ in range(n)]

        # n-3因为j至少要从n+2开始
        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                res = inf
                for k in range(i+1, j-1):
                    res = min(res, f[i][k]+f[i][j]+v[i]*v[j]*v[k])
                f[i][j] = res # type: ignore
        return f[0][n-1] # type: ignore