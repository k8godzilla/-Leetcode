#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:20:04 2019

@author: sunyin
"""

'''
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def maxProduct(self, nums : list):
        res0 = self.maxProductSub(nums)
        nums.reverse()
        res1 = self.maxProductSub(nums)
        return max(res0, res1)
    
    
    def maxProductSub(self, nums: list) -> int:
        # maxProduct(self, nums: List[int]) -> int:
        

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        self.dp = [0] * len(nums)
        self.dp[0] = nums[0]
            
        if nums[0] < 0:
            iNeg = 0
        else:
            iNeg = -1
        
        for i in range(1, len(nums)):
            if nums[i] > 0:
                if self.dp[i - 1] > 0:
                    self.dp[i] = self.dp[i - 1] * nums[i]
                else:
                    self.dp[i] = nums[i]

            elif nums[i] < 0:
                if iNeg == -1:
                    iNeg = i
                    self.dp[i] = nums[i]
                else:
                    t = self.dp[iNeg] * nums[i]
                    if self.dp[i - 1] > 0:
                        t *= self.dp[i - 1]
                    if self.dp[iNeg - 1] > 0:
                        t *= self.dp[iNeg - 1]
                    self.dp[i] = t
                    iNeg = -1
            else:
                iNeg = -1
                
        
        return max(self.dp)


                
cl = Solution()
nums = [-2,0,-1, 10]
res = cl.maxProduct(nums)        
            
        
        




