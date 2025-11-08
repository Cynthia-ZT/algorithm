# 给你一个按照非递减顺序排序的整数数组nums，和一个目标值target。
# 请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值target，返回[-1, -1]。
# 你必须设计并实现时间复杂度为O(log n)的算法解决此问题。

class Solution:
    # 时间复杂度：0(log n)，空间复杂度：0(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(self, nums: List[int], target: int) -> int:
            n = len(nums)
            left = -1
            right = n
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid # (mid, R)
                else:
                    right = mid # (L, mid)
            return right
        start = lower_bound(self, nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound(self, nums, target + 1) - 1
        # 由于start存在，所以end一定存在
        return [start, end]