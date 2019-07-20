# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 18:24:22 2019

@author: admin
"""

'''
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5 
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
说明:

你的解法应该是 O(logN) 时间复杂度的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def findPeakElement(self, nums: list) -> int:
        # findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        a = pow(2, -30)
        nums = [a] + nums + [a]
        
        res = self.findPeakElementRecursive(nums, 0, len(nums) - 1)
        return res - 1
    
    def findPeakElementRecursive(self, nums:list, i:int, j:int) -> int:
        if j - i == 2:
            if nums[i + 1] > nums[i] and nums[i + 1] > nums[j]:
                return i + 1
            else:
                return -1
        else:
            k = (i + j) // 2
            if nums[k + 1] > nums[k]:
                if j - k >= 2:
                    idx = self.findPeakElementRecursive(nums, k, j)
                    if idx != -1:
                        return idx
            elif nums[k - 1] > nums[k]:
                if k - i >= 2:
                    idx = self.findPeakElementRecursive(nums, i, k)
                    if idx != -1:
                        return idx
            else:
                return k
        return -1
                
        
        
cl = Solution()
nums =  [3,2,1]
res = cl.findPeakElement(nums)      
        
        
        
        
        
        
        
        
        
        
