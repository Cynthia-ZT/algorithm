# 给你一个字符串s，请你将s分割成一些子串，使每个子串都是回文串。返回s所以可能的分割方案。
# 回文串是正着读和反着读都一样的字符串。

# 枚举“a,a,b”的这两个逗号，选或不选，就转换成了子集型问题
# ["aab"]， ["a","ab"]，["aa","b"]，["a","a","b"]
# 按照答案的视角分析
# 枚举第一个逗号的位置(或者没有)
# 枚举第二个逗号的位置（或者没有）
# 当前操作？选择回文子串s[i..j]，加入path
# 子问题？从下标>=i的后缀中构造子集
# 下一个子问题？从下标>=j+1的后缀中构造回文分割

from typing import List


class Solution:
    # 时间复杂度O(n*2^n)，空间复杂度(n)
    def partition(self, s: str) -> List[List[str]]:
        def isSymmetric(s: str):
            n = len(s)
            left = 0
            right = n - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        path = []
        ans = []
        n = len(s)
        def dfs(i):
            if i == n:
                ans.append(''.join(path.copy()))
            for j in range(i, n):
                t = s[i:j+1]
                if isSymmetric(t):
                    path.append(s[j])
                    dfs(i+1)
                    path.pop()

        dfs(0)
        return ans