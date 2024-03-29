# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:41:57 2019

@author: admin
"""

'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]


'''

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0: break # because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]: continue # skip.
            i, j = k + 1, len(nums) - 1
            step = 50
            status = 0
            if j - i > 2 * step:
                while j - i > step:
    
                    s = nums[k] + nums[i] + nums[j]
                    if s < 0:
                        if status == 1:
                            j += step
                            status = 0
                            break
                        else:
                            i += step
                            status = -1
                    elif s > 0:
                        if status == -1:
                            i -= step
                            status = 0
                            break
                        else:
                            j -= step
                            status = 1
                    else:
                        break
    
                if status == 1:
                    j += step
                elif status == -1:
                    i -= step
            
         

            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res
        