#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:11:18 2019

@author: sunyin
"""

'''
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 本问题的关键在于 是否认识到 x > y <=> x + y > y + x具有传导性



class Solution:
    def largestNumber(self, nums: list) -> str:
        # def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        numsSort = self.mergeSort(nums)
        if numsSort[0] == '0':
            return '0'
        return ''.join(numsSort)
    
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        else:
            iM = len(nums) // 2
            num0, num1 = self.mergeSort(nums[:iM]), self.mergeSort(nums[iM:])

            numMerge = []
            i, j = 0, 0
            while i < len(num0) or j < len(num1):
               
                if i >= len(num0):
                    numMerge.extend(num1[j:])
                    j = len(num1)
                elif j >= len(num1):
                    numMerge.extend(num0[i:])
                    i = len(num0)
                elif self.compare(num0[i], num1[j]):
                    numMerge.append(num0[i])
                    i += 1
                else:
                    numMerge.append(num1[j])
                    j += 1
            return numMerge
            
        
    def compare(self, n1, n2):
        return n1 + n2 > n2 + n1
        
        
        

cl = Solution()
nums = [3,30,34,5,9]
res = cl.largestNumber(nums)


nums = ['1', '2']
a = cl.mergeSort(nums)
