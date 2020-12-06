#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (48.96%)
# Likes:    704
# Dislikes: 0
# Total Accepted:    238.9K
# Total Submissions: 487.6K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 
# 
# 
# 说明：
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 
# 
# 示例：
# 
# 
# 输入：
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出：[1,2,2,3,5,6]
# 
# 
# 
# 提示：
# 
# 
# -10^9 
# nums1.length == m + n
# nums2.length == n
# 
# 
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ## from end to start, O(n)
        tailn, tailm, tail = n-1, m-1, m+n-1
        while(tailn>=0 and tailm>=0):
            greater = max(nums2[tailn],nums1[tailm])
            nums1[tail] = greater
            tail -= 1
            if greater == nums1[tailm]: tailm -= 1
            else: tailn -= 1
        for i in range(tailn+1):
            nums1[i] = nums2[i]
        return nums1



# @lc code=end

