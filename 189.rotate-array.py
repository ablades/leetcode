#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (34.64%)
# Likes:    3070
# Dislikes: 837
# Total Accepted:    521.1K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
# 
# Follow up:
# 
# 
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# It's guaranteed that nums[i] fits in a 32 bit-signed integer.
# k >= 0
# 
# 
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        shifts = 0
        current_index = 0
        current_value = nums[0]
        next_index = (current_index + k) % len(nums)
        next_value = nums[next_index]
        # shift until all have been shifted
        while shifts < len(nums):
            print(f'c_index:{current_index}, c_value:{current_value}, n_index:{next_index}, n_value:{next_value}, shifts:{shifts}  \n')
            next_value = nums[next_index]
            nums[next_index] = current_value
            current_value = next_value
            current_index = next_index
            next_index = (current_index + k) % len(nums)
            shifts += 1