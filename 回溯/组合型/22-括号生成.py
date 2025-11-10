# 数字n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。

# 从2n个位置中选n个位置放左括号
# 左括号等价于选，有括号等价于不选

# 回溯三问
# 当前操作？枚举path[i]是左括号还是有括号
# 子问题？构造字符串>=i的部分
# 下一个子问题？构造字符串>=i+1的部分

# 还需要记录左括号的个数open，从而方便判断
# 需要选n个左括号
# 只要open<n就可以选左括号

# 右括号的个数为i-open
# 如果右括号的个数小于左括号的个数
# 即i-open<open，就可以选有括号
# dfs(i, open)
#   ·dfs(i+1,open+1)选左括号
#   ·dfs(i+1,open)选有括号

from typing import List


class Solution:
    # 时间复杂度O(n*C(2n,n)), 空间复杂度O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2*n
        ans = []
        path = [''] * m
        def dfs(i, open):
            if i == m:
                ans.append(''.join(path))
                return
            if open < n:
                path[i] = '('
                dfs(i+1, open+1)
            if i-open < open:
                path[i] = ')'
                dfs(i+1, open)
        dfs(0, 0)
        return ans