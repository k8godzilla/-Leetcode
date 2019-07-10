#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 22:21:41 2019

@author: sunyin
"""

'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


'''

class Solution:
    def permute(self, nums):
        '''
        nums : List[int]
        return : List[List[int]]
        '''
        res = []
        idx = list(range(len(nums)))
        combs = 1
        for i in range(len(nums)):
            combs *= (1 + i)
        
        
        for i in range(combs):
            num_i = []
            for j in range(len(idx)):
                num_i.append(nums[idx[j]])
            res.append(num_i)
            self.idxNext(idx)
                
  
        return res
        
    
        
    def idxNext(self, idx):
        
        idx_left = 1
        for i in range(len(idx) - 1):
            if idx[-1 - i] > idx[-2 - i]:
                idx_left = -2 - i
                break
        
        if idx_left < 1:
            for i in range(len(idx) - 1):
                if idx[-1 - i] > idx[idx_left]:
                    idx_right = -1 - i
                    break
        
            cache = idx[idx_left]
            idx[idx_left] = idx[idx_right]
            idx[idx_right] = cache
            i, j = idx_left + 1, -1
        else:
            i, j = (-1) * len(idx), -1
            
        while i < j:
            cache = idx[i]
            idx[i] = idx[j]
            idx[j] = cache
            i += 1
            j -= 1

            
cl = Solution()
          
nums = [1, 2, 3]      
  
res = cl.permute(nums)   
        
        
        
        
        
        
        
        

