# 给你一个整数数组nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的k个数字。滑动窗口每次只向右移动一位。
# 返回滑动窗口中的最大值。

# 需要一个数据结构
# 单调队列：
#   双端队列
#       移除最左边的元素
#       移除最右边的元素
#       在最右边插入元素
#   单调性
#       从队首到队尾单调递减

from collections import deque
from typing import List


class Solution:
    # 时间复杂度O(n)，
    # 空间复杂度O(k)，更准确的,U=(len(set(nums))) O(min(k,U))
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        
        for i, x in enumerate(nums):
            # 1. 入
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)

            # 2. 出
            if i-q[0] >= k:
                q.popleft()
            
            # 3. 记录答案
            if i >= k-1:
                ans.append(nums[q[0]])
        return ans
    # 及时去掉无用数据，保证双端队列有序。
    #   当前数字>=队尾，弹出队尾（和单调栈一样）
    #   弹出队首不在爽口内的元素
    