# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:42:05 2019

@author: admin
"""

'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pool = set()
        for i in range(len(nums)):
            if nums[i] in pool:
                return True
            else:
                pool.add(nums[i])
            if i - k >= 0:
                pool.remove(nums[i - k])
        return False
        


cl = Solution()
nums = [1,2,3,1,2,3]
k = 2
res = cl.containsNearbyDuplicate(nums, k)



