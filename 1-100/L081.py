#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 20:12:33 2019

@author: sunyin
"""

class Solution:
    def search(self, nums, target):
        # nums : List[int]
        # target : int
        # return : bool
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return nums[0] == target
        change_ex, change_idx = self.searchChange(nums, 0, len(nums) - 1)
        print(change_ex, change_idx)

        if change_ex:
            res = self.searchPoints(nums, 0, change_idx - 1, target)
            if res:
                return res
            else:
                return self.searchPoints(nums, change_idx, len(nums) - 1, target)
        else:
            return self.searchPoints(nums, 0, len(nums) - 1, target)
                
        
        
    def searchPoints(self, nums, i, j, target):
        if target < nums[i] or target > nums[j]:
            return False
        while i <= j:
            i_m = (i + j) // 2
            if nums[i_m] == target:
                return True
            elif nums[i_m] < target:
                i = i_m + 1
            else:
                j = i_m - 1
        return False
            
        
        
        
        
        
        
    def searchChange(self, nums, i, j):
        i_init, j_init = i, j
        print(i, j)
        if j - i == 0:
            return False, -1
        elif j - i == 1:
            if nums[i] >= nums[0] and nums[j] < nums[0]:
                return True, j
            if nums[i] > nums[0] and nums[j] <= nums[0]:
                return True, j
        
        while i <= j:
            i_m = (i + j) // 2
            print('i_m', i_m)
            if i_m + 1 >= len(nums):
                break
            if nums[i_m] < nums[0]:
                j = i_m - 1
            elif nums[i_m + 1] > nums[0]:
                i = i_m + 1
            elif nums[i_m]  == nums[0] and nums[i_m+1] == nums[0]:

                b, idx = self.searchChange(nums, i_init, i_m - 1)
                if b:
                    return b, idx
                else:

                    b, idx = self.searchChange(nums, i_m+ 1, j_init)
                    return b, idx
            else:
                return True, i_m + 1
        return False, -1
    
    
    
    
    
cl = Solution()
    
nums = [2,2,2,0,0,1,1]
target = 0

res = cl.search(nums, target)   
    
            
                    