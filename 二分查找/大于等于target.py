# 返回有序数组中第一个>=target的数的位置，如果所有数都<target，返回数组长度。
# 红蓝染色法
# 求闭区间[left, right]
# L和R分别指向询问的左右边界，即闭区间[L, R]
# M指向中点位置mid = (L + R) // 2，表示当前正在询问的数
# 红色背景表示false，即<target
# 蓝色背景表示true，即>=target
# 白色表示不确定

# 时间复杂度：0(log n)，空间复杂度：0(1)
def lower_bound_both_close(nums: List[int], target: int) -> int:
    n = len(nums)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1 # [mid + 1, R]
        else:
            right = mid - 1 # [L, mid - 1]
    # 关键循环不变量
    # L-1始终是红色
    # R+1始终是蓝色
    # 所以 R+1 是我们要的答案
    # 由于循环到结束的时候，L在R的右边一个位置，所以答案也可以是L
    return left

def lower_bound_right_open(nums: List[int], target: int) -> int:
    # 求左闭右开的区间[left, right)
    n = len(nums)
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1 # [mid + 1, R)
        else:
            right = mid # [L, mid)
    return left # 或者 return right

def lower_bound_left_open(nums: List[int], target: int) -> int:
    # 求左开右闭的区间(left, right]
    n = len(nums)
    left = -1
    right = n - 1
    while left < right:
        mid = (left + right + 1) // 2
        if nums[mid] < target:
            left = mid # (mid, R]
        else:
            right = mid - 1 # (L, mid - 1]
    return right + 1

def lower_bound_both_open(nums: List[int], target: int) -> int:
    # 求左开右开的区间(left, right)
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

# 延伸到
# > target 相当于 (>= target + 1)
# < target 相当于 (>= target) 的结果过 - 1
# <= target 相当于 (> target)的结果 - 1，也就是 (>= target + 1)的结果-1