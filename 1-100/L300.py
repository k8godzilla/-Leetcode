# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:56:54 2019

@author: admin
"""

'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def lengthOfLIS(self, nums: list) -> int:
    # def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        maxLen = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > maxLen[-1]:
                maxLen.append(nums[i])
            elif nums[i] > maxLen[0]:
                idx = self.binaryInsert(maxLen, nums[i])
                maxLen[idx + 1] = min(maxLen[idx + 1], nums[i])
            else:
                maxLen[0] = nums[i]
        return len(maxLen)
            
            
    def binaryInsert(self, maxLen, target):
        i, j = 0, len(maxLen) - 1
        while i <= j:
            if j - i <= 1:
                if maxLen[j] < target:
                    return j
                else:
                    return i
            else:
                iM = (i + j) // 2
                if maxLen[iM] < target and maxLen[iM + 1] >= target:
                    return iM
                elif maxLen[iM] >= target:
                    j = iM
                else:
                    i = iM
 


                   
nums = [10,9,2,5,3,7,101,18]       
cl = Solution()
res = cl.lengthOfLIS(nums)     
        
        
        
        
        




