#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (57.79%)
# Likes:    4072
# Dislikes: 129
# Total Accepted:    886.8K
# Total Submissions: 1.5M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        next_zero = 0
        last_digit = 0

        while next_zero < len(nums) and last_digit < len(nums):

            # indexes have crossed, swap needs to occur
            if next_zero > last_digit:
                nums[next_zero], nums[last_digit] = nums[last_digit], nums[next_zero]
            # indexes have not crossed, means weve hit a zero in correct place, advance next_zero
            else:
                next_zero += 1

            while next_zero < len(nums):
                #have found a zero
                if nums[next_zero] == 0:
                    break
                else:
                    next_zero += 1
            
            while last_digit < len(nums):
                # have found a digit
                if nums[last_digit] > 0:
                    break
                else:
                    last_digit += 1

        #two pointers 
        #one keeps track of last zero seen
        #other keeps track of next digit to swap
        #if zero pointer crosses digit pointer we need to swap. 
        #swap and continue
        
# @lc code=end
