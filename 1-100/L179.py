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



class Solution:
    def largestNumber(self, nums: list) -> str:
        # def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        
        nums = [str(nums[i]) for i in range(len(nums))]
        
        self.groups = [[] for i in range(9)]
        
        for i in range(len(nums)):
            idx = int(nums[i][0])
            self.groups[idx - 1].append(nums[i])
            
        res = ''
        for i in range(len(self.groups)):
            if self.groups[i] != []:
                res = self.groupCompete(self.groups[i], str(i + 1), res)
        return res
            
        
        
    def groupCompete(self, nums, digitFill,a):
        numsNew = [nums[i] + a for i in range(len(nums))]
        lenMax = max([len(numsNew[i]) for i in range(len(numsNew))])
        numsNew = [numsNew[i] + digitFill * (lenMax - len(numsNew[i])) for i in range(len(numsNew))]
        d = {}
        for i in range(len(numsNew)):
            d[numsNew[i]] = i
        numsNewSort = self.numberBattle(numsNew, 0)
        res = ''
        print(nums)
        for i in range(len(numsNewSort)):
            res += nums[d[numsNewSort[i]]]

        return res + a
        
    def numberBattle(self, nums, idx):
        if idx >= len(nums[0]):
            return nums
        
        numsSort = []
        pool = [[] for i in range(10)]
        for i in range(len(nums)):
            idxPool = int(nums[i][idx])
            pool[idxPool].append(nums[i])
        
        for i in range(9, -1, -1):
            if len(pool[i]) == 1:
                numsSort.append(pool[i][0])
            elif len(pool[i]) > 1:
                numNext = self.numberBattle(pool[i], idx + 1)
                for j in range(len(numNext)):
                    numsSort.append(numNext[j])
        return numsSort
            


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
        
cl = Solution()       
     

   
nums = [121,12]
res = cl.largestNumber(nums)           






