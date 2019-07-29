# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:36:33 2019

@author: admin
"""

'''
给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。

示例：

输入: nums = [-2,0,1,3], target = 2
输出: 2 
解释: 因为一共有两个三元组满足累加和小于 2:
     [-2,0,1]
     [-2,0,3]
进阶：是否能在 O(n2) 的时间复杂度内解决？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-smaller
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def threeSumSmaller(self, nums: list, target: int) -> int:
        # def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            resDouble = self.doublePointer(nums, i + 1, len(nums) - 1, target - nums[i])
            res += resDouble
        return res
        
        
    def doublePointer(self, nums, j, k, target):
        res = 0
        while j < k:
            if nums[j] + nums[k] < target:
                res += (k - j)
                j += 1
            else:
                k -= 1
        return res




cl = Solution()
nums = [6,7,-5,-2,9,2,-10,-14,-5,4,6,-3,5,3,6,7,-15,8,2,-6,-7,-10,2,-10,3,12,-10,11,8,5,8,-14,-3,12,3,-4,-9,-10,0,-13,12,-14,4,-3,-3,14,0,-14,10,-4,11,-6,9,2,13,2,13,12,-7,3,3,2,13,2,11,-10,-2,-13,-5,14,-3,5,-15,3,1,3,3,6,5,13,-4,-2,2,-1,-15,-12,-5,1,-12,3,-12,14,0,-15,-13,-10,-7,-15,-2,1,11,-4,-1,-1,-15,11,-11,-1,-15,-6,-6,-14,-12,-5,5,7,9,-8,-11,9,14,-11,11,6,1,5,-14]
target = 8

res = cl.threeSumSmaller(nums, target)
