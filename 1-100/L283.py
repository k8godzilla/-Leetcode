# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:20:19 2019

@author: admin
"""

'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 找到第一个零
        hasZero = False
        for i in range(len(nums)):
            if nums[i] == 0:
                hasZero = True
                break
            
        if hasZero:
            p = i
            for j in range(i + 1, len(nums)):
                if nums[j] != 0:
                    nums[p] = nums[j]
                    nums[j] = 0
                    p += 1
                    
                    
cl = Solution()
nums = [0,1,0,3,12]
cl.moveZeroes(nums)
                    
                    
                    
                    
            
            
            
            
        
        
        
        






