# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:03:10 2019

@author: admin
"""

'''
给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。

示例 1:

输入: [0,1,2,4,5,7]
输出: ["0->2","4->5","7"]
解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
示例 2:

输入: [0,2,3,4,6,8,9]
输出: ["0","2->4","6","8->9"]
解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/summary-ranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def summaryRanges(self, nums: list) -> list:
    # def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        
        idx = 0
        res = []
        while idx < len(nums):
            s, idx = self.helper(nums, idx)
            res.append(s)
        return res
    
    def helper(self, nums, idx):
        cStart, cEnd = nums[idx], nums[idx]
        while idx + 1 < len(nums):
            if nums[idx + 1] - nums[idx] == 1:
                cEnd = nums[idx + 1]
                idx += 1
            else:
                break
        if cEnd == cStart:
            return str(cStart), idx + 1
        else:
            s = str(cStart) + '->' + str(cEnd)
            return s, idx + 1
            


cl = Solution()
nums = [0,2,3,4,6,8,9]
res = cl.summaryRanges(nums)
