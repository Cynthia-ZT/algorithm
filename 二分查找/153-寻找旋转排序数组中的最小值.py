# 已知一个长度为n的数组，预先按照升序排列，经由1到n次旋转后，得到输入数组。例如，原数组nums = [0,1,2,4,5,6,7]在变化后可能得到：
# 若旋转4次，则可以得到[4,5,6,7,0,1,2]
# 若旋转7次，则可以得到[0,1,2,4,5,6,7]
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
# 给你一个元素值互不相同的数组nums，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的最小元素。
# 你必须设计一个时间复杂度为O(log n)的算法解决此问题。

# 红蓝染色法
# 红色背景表示false，即最小值的左侧
# 蓝色背景表示true，即最小值及其右侧
class Solution:
    # 时间复杂度：0(log n)，空间复杂度：0(1)
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = -1
        right = n
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid  # (L, mid)
            else:
                left = mid  # (mid, R)
        return nums[right]