class Solution:
    def subListProductLessThanTarget(self, nums, k) -> int:
        # 易忽略点
        # 考虑不需要遍历的情况
        # 时间复杂度O(n), 空间复杂度O(1)
        
        if k <= 1:
            return 0
        
        prod = 0
        left = 0
        ans = 0
        for right, x in enumerate(nums):
            prod *= x
            while prod >= k:
                prod /= nums[left]
                left += 1
            # 一个数组的子数组个数等于这段数组的元素个数
            ans += right - left + 1
        return ans