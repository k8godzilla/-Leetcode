# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:38:58 2019

@author: admin
"""

'''
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def longestConsecutive(self, nums):
        if len(nums) <= 1:
            return len(nums)
        
        nMin, nMax = nums[0], nums[0]
        for i in range(1, len(nums)):
            nMin = min(nMin,  nums[i])
            nMax = max(nMax, nums[i])
            
        if nMin == nMax:
            return 1
        h = [0] * (nMax - nMin + 1)
        for i in range