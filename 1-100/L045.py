# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:28:13 2019

@author: admin
"""

'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。


'''


class Solution:
    def jump(self, nums):
        ### nums : List[int]
        ### return : int
        if  len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 1
        
        steps = [0] * len(nums)
        for i in range(1, len(nums)):
            step_i = nums[-1 -i]
            if step_i == 0:
                steps[-1-i] = len(nums)
            else:
                if -1 -i + step_i >= -1:
                    ps = 1
                else:
                    ps = steps[-1-i + step_i] + 1
                steps[-1-i] = ps
            self.stepUpdate(steps, -1-i)
            
                
                
        return steps[0]
    
    def stepUpdate(self, steps, idx):
        v_update = steps[idx]
        idx += 1
        while idx < -1:
            if steps[idx] > v_update:
                steps[idx] = v_update
                idx += 1
            else:
                break
    
 
            
            
                
            
            
cl = Solution()
nums = [1] * 10000
res =  cl.jump(nums)          
            
            

        
        
        
        
        
        
        
        
        
        