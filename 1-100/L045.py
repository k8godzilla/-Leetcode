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
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
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
        step_record = {}
        step_record[0] = -1
        key_list = [0]
        for i in range(1, len(nums)):
            step_i = nums[-1 -i]
            if step_i == 0:
                steps[-1-i] = len(nums)
            else:
                ps = self.findMinPossibleStep(step_record, -1-i, step_i, key_list)

                steps[-1-i] = ps + 1
                try:
                    step_record[ps + 1] = min(step_record[ps + 1],-1-i)
                except:
                    step_record[ps + 1] = -1 -i
                    if ps + 1 < key_list[-1]:
                        key_list.append(ps + 1)
                        key_list.sort()
                        
                    else:
                        key_list.append(ps + 1)
            
 
        return steps[0]
    
    def findMinPossibleStep(self, step_record, idx, step, key_list):
        for i  in range(len(key_list)):
            key = key_list[i]
            if step_record[key] <= idx + step:
                return key
        return len(nums)
            
            
                
            
            
cl = Solution()
nums = [1] * 10000
res =  cl.jump(nums)          
            
            

        
        
        
        
        
        
        
        
        
        