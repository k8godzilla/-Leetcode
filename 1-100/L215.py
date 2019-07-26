# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:05:54 2019

@author: admin
"""

'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:

        # findKthLargest(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        numMin, numMax = nums[0], nums[0]
        for i in range(1, len(nums)):
            numMin = min(numMin, nums[i])
            numMax = max(numMax, nums[i])
            
        
            
        if k == 1 or numMin == numMax:
            return numMax
        
        gap = numMax - numMin
        gap = min(gap, 100)
        
        cache = [[] for _ in range(gap + 1)]
        for i in range(len(nums)):
            idx = int((nums[i] - numMin) / (numMax - numMin) * (gap))
            cache[idx].append(nums[i])
        


        count = 0
        for i  in range(len(cache) - 1, -1, -1):
            count += len(cache[i])
            if count >= k:
                break
            
        if len(cache[i]) == 1:
            return cache[i][0]
        elif i == len(nums) - 1:
            return self.findKthLargest(cache[-1], k)
        else:
            count -= len(cache[i])
            return self.findKthLargest(cache[i], k - count)
        
        
import numpy as np 
        
cl = Solution()
nums = np.arange(5000).tolist()
k = 5000
res = cl.findKthLargest(nums, k) 
        
        
        
        
        
        
        
        
        
        
        
            
            

