# 给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按任意顺序返回。
# 给出数字对字母的映射与9键电话按键相同。注意1不对应任何字母

from typing import List


MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    # 时间复杂度O(n*4^n)，最多的时候要嵌套4次循环，每次求答案要递归一次需要O(n)
    # 空间复杂度O(n)，因为递归要记录每次的结果
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        
        ans = []
        path = [''] * n
        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return 
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i+1)
        dfs(0)
        return ans
