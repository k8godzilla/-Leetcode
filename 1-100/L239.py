# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:36:19 2019

@author: admin
"""

'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
注意：

你可以假设 k 总是有效的，1 ≤ k ≤ 输入数组的大小，且输入数组不为空。

进阶：

你能在线性时间复杂度内解决此题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if k <= 1:
            return nums
        
        # 初始化第一个窗口
        idxCache = [0]
        
        for i in range(1, k):
            if nums[i] > nums[idxCache[0]]:
                idxCache = [i]
            else:
                for j in range(len(idxCache) - 1, -1, -1):
                    if nums[idxCache[j]] >= nums[i]:
                        break
                if j < len(idxCache) - 1:
                    idxCache = idxCache[:j + 1] + [i]
                else:
                    idxCache.append(i)
                    
        res = [nums[idxCache[0]]]
        for i in range(k, len(nums)):           
            if i - idxCache[0] >= k:
                idxCache = idxCache[1:]
            
            if nums[i] > nums[idxCache[0]]:
                idxCache = [i]
            else:
                for j in range(len(idxCache) - 1, -1, -1):
                    if nums[idxCache[j]] >= nums[i]:
                        break
                if j < len(idxCache) - 1:
                    idxCache = idxCache[:j + 1] + [i]
                else:
                    idxCache.append(i)
            res.append(nums[idxCache[0]])
            
       
        return res
    
cl = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 2
res = cl.maxSlidingWindow(nums, k)           
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    