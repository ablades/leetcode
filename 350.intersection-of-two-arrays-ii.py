#
# @lc app=leetcode id=350 lang=python
#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (51.33%)
# Likes:    1501
# Dislikes: 427
# Total Accepted:    377K
# Total Submissions: 733.1K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# 
# 
# Note:
# 
# 
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
# 
# 
# Follow up:
# 
# 
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
# 
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #sorted solution
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        inter = list()

        i = 0
        j = 0

        while(i < len(nums1) and j < len(nums2)):

            if nums1[i] == nums2[j]:
                inter.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return inter

        #iterate over both lists
        #compare values
        #if equal add value to new list
        # increment the lower pointer
        #repeat
        
# @lc code=end
