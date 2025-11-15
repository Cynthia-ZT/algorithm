# 给你一个整数数组nums，数组中的元素互不相同。返回该数组所有可能得子集(幂集)。
# 解集不能包含重复的子集。你可以按任意顺序返回解集。

# 子集型回溯

from typing import List

# 每个元素都可以选或不选:
# 站在输入的角度思考:ß
# 每个数可以在子集中(选)
# 也可以不在子集中（不选）
# 叶子就是答案
# 当前操作？枚举第i个数选或不选
# 子问题？从下标>=i的数字中构造子集
# 下一个子问题？从下表>=i+1的数字中构造子集
class Solution:
    # 时间复杂度O(n*2^n)，因为每个元素有选或不选两种情况，然后每次遍历的时候还有copy的时间O(n)
    # 空间复杂度O(n)
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        def dfs(i):
            # 边界条件
            if i == n:
                # 用copy是因为path是一个全局变量，所以值后面可能变
                ans.append(''.join(path.copy()))
                return

            # 不选，跳过，递归到i+1
            dfs(i+1)

            # 选，加到路径中，在递归i+1
            path.append(nums[i])
            dfs(i+1)
            # 要回复path，因为递归i+1的时候path会加上i+1的数
            path.pop()

        dfs(0)
        return ans
    
    # 每个元素必须选：
    # 站在答案的角度思考：
    # 枚举第一个数选谁
    # 枚举第二个数选谁
    # 每个结点都是答案
    # 当前操作？枚举一个下标j>=i的数字(因为答案不考虑顺序，这里就规定了一个顺序)，加入path
    # 子问题？从下标>=i的数字构造子集
    # 下一个子问题？从下标>=j+1的数字中构造子集
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        def dfs(i):
            ans.append(''.join(path.copy()))
            if i == n:
                return
            for j in range(i, n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return ans
