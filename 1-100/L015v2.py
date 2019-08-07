# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:43:38 2019

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
    def threeSum(self, nums:list):
        nums.sort()
        self.nums = nums
        self.res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                self.twoPointer(nums[i], i + 1, (-1) * self.nums[i])
        return self.res
        
    def twoPointer(self, v, j, target):
        k = len(self.nums) - 1
        while j < k:
            if self.nums[j] + self.nums[k] == target:
                self.res.append([v, self.nums[j], self.nums[k]])
                j += 1
                while j < k and self.nums[j] == self.nums[j - 1]:
                    j += 1              
            elif self.nums[j] + self.nums[k] < target:
                j += 1
                while j < k and self.nums[j] == self.nums[j - 1]:
                    j += 1 
            else:
                k -= 1
                while j < k and self.nums[k] == self.nums[k + 1]:
                    k -= 1