# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 08:22:57 2019

@author: admin
"""

'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
说明：

这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def findMin(self, nums: list) -> int:
        # findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            if nums[0] < nums[1]:
                return nums[0]
            else:
                return nums[1]
        else:
            if nums[0] < nums[-1]:
                return nums[0]
            i, j = 0, len(nums) - 1
            while i <= j:
                if j - i <= 1:
                    if nums[j] < nums[i]:
                        return nums[j]
                    else:
                        return nums[i]
                else:
                    iM = (j + i) // 2
                    if nums[iM] == nums[0]:
                        min0 = self.findMin(nums[:iM])
                        min1 = self.findMin(nums[iM:])
                        return min(min0, min1)
                    elif nums[iM] < nums[iM - 1]:
                        return nums[iM]
                    elif nums[iM] > nums[0]:
                        i = iM
                    else:
                        j = iM

cl = Solution()
                        
nums = [1,3,5]

res = cl.findMin(nums)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
    
    
    