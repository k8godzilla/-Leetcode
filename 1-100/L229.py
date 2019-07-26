# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:26:05 2019

@author: admin
"""

'''
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def majorityElement(self, nums: list) -> list:
    # def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        if len(nums) == 2:
            return list(set(nums))
        
        res = []
        c = len(nums) // 3
        d = {}
        for i in range(len(nums)):
            try:
                d[nums[i]] += 1
                if d[nums[i]] > c:
                    res.append(nums[i])
            except:
                d[nums[i]] = 1
        return list(set(res))
                
                
cl = Solution()
nums =   [1,2,3]      
res = cl.majorityElement(nums)     
                
        
        
        
        
        
        
        
        
        
        
