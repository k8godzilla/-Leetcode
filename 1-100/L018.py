# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:41:00 2019

@author: admin
"""

'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def fourSum(self, nums, target):
        '''
        nums : List[int],
        target: int
        return : List[List[int]]
        '''
        if len(nums) < 4:
            return []
        
        res = []
        i0 = 0
        nums.sort()
        while nums[i0] <= target / 4 and len(nums) - 1 - i0 > 2:
            i3 = len(nums) - 1
            while i0 + 1 < i3 - 1:
                sub_target = target - nums[i0] -nums[i3]
                
                res_sub = self.doublePointerSearch(nums, i0 + 1, i3 - 1, sub_target, nums[i0], nums[i3])
                for r in res_sub:
                    res.append(r)
                i3 -= 1
                while i3 - i0 > 2 and nums[i3] == nums[i3 + 1]:
                    i3 -= 1
            i0 += 1
            while len(nums) - 1 - i0 > 2 and nums[i0] == nums[i0 - 1]:
                i0 += 1 
        
       
        return res
            
            
    def doublePointerSearch(self,nums, i_start, i_end, sub_target, v0, v3):
        res = []
        if nums[i_start] > sub_target / 2 or nums[i_end] < sub_target / 2:
            return res
        step = 50
        status = 0
        if i_end - i_start > 2 * step:
            while i_end - i_start > step:
                s = nums[i_start] + nums[i_end] - sub_target
                if s < 0:
                    if status == 1:
                        i_end += step
                        status = 0
                        break
                    else:
                        i_start += step
                        status = -1
                elif s > 0:
                    if status == -1:
                        i_start -= step
                        status = 0
                        break
                    else:
                        i_end -= step
                        status = 1
                else:
                    break
    
            if status == 1:
                i_end += step
            elif status == -1:
                i_start -= step
            
        while i_start < i_end:
            s = nums[i_start] + nums[i_end] - sub_target
            if s < 0:
                i_start += 1
                while i_start < i_end and nums[i_start] == nums[i_start - 1]: i_start += 1
            elif s > 0:
                i_end -= 1
                while i_start < i_end and nums[i_end] == nums[i_end + 1]: i_end -= 1
            else:
                res.append([v0, nums[i_start], nums[i_end], v3])
                i_start += 1
                i_end -= 1
                while i_start < i_end and nums[i_start] == nums[i_start - 1]: i_start += 1
                while i_start < i_end and nums[i_end] == nums[i_end + 1]: i_end -= 1
        return res
            
        


        
        
        
        
        
        
        
        
        
        