#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 19:13:00 2019

@author: sunyin
"""

'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定 nums = [1,1,1,2,2,3],

函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,1,2,3,3],

函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def removeDuplicates(self, nums) :
        # nums : List[int]
        # returen : int
        if len(nums) == 0:
            return 0
        
        mem = nums[-1] + 1
        count = 0
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != mem:
                mem = nums[j]
                nums[i] = mem
                i += 1
                count = 1
            elif count < 2:
                nums[i] = mem
                i += 1
                count += 1
            j += 1
            
        return i 
    
cl = Solution()
res = cl.removeDuplicates([1])