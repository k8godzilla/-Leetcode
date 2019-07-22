# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:30:22 2019

@author: admin
"""

'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        
'''

class Solution:
    def minSubArrayLen(self, s: int, nums: list) -> int:
        # minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        self.s = s
        
        if len(nums) == 0:
            return 0
        
        self.cuSum = [0]
        
        for i in range(len(nums)):
            self.cuSum.append(self.cuSum[-1] + nums[i])
            
        if self.cuSum[-1] < s:
            return 0
        
        # initialize max Length
        for i  in range(1, len(self.cuSum)):
            if self.cuSum[i] >= s:
                lenMax = self.lenMaxExplore(i, i)
                break
            
        
        if lenMax == 1:
            return lenMax
        
        for j  in range(i + 1, len(self.cuSum)):
            if self.cuSum[j] - self.cuSum[j - lenMax + 1] >= s:
                lenMax = self.lenMaxExplore(j, lenMax)
                if lenMax == 1:
                    break
        
        return lenMax
        
        
        
    def lenMaxExplore(self,i, lenMax):
        c = 0
        while self.cuSum[i] - self.cuSum[i - lenMax + c] >= self.s:
            c += 1
        return lenMax - c + 1
        
        
        
        
cl = Solution()
s = 9
nums = [2,3,1,2,4,3]       
        
lenMax = cl.minSubArrayLen(s, nums)
        
        
        
        
        
        
        
        
        
        
        

