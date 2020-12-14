#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        level = [root]
        res = []
        while level:
            nextLevel = []
            filtered = list(filter(lambda x: x is not None, level))
            res.append(list(map(lambda x: x.val, filtered)))
            for node in filtered:
                nextLevel += node.children
            level = nextLevel

        return res

# @lc code=end

