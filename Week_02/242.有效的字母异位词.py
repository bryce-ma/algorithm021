#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1,set2 = {},{}
        for c in s:
            set1[c] = set1.get(c, 0) + 1
        for c in t:
            set2[c] = set2.get(c, 0) + 1
        return set1.keys() == set2.keys() and all(map(lambda k: set2[k] == set1[k],set1.keys()))

# @lc code=end

