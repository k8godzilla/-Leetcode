# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 15:28:49 2019

@author: admin
"""

'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
在真实的面试中遇到过这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def rotate(self, nums: list, k: int) -> None:
        # rotate(self, nums: List[int], k: int) -> None
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k != 0:
            iStart = 0
            while iStart <= len(nums) - k -1:
                for i in range(k - 1, -1, -1):
                    
                    cache = nums[-1 - i]
                    nums[-1-i] = nums[k - 1 - i + iStart]
                    nums[k - 1 - i + iStart] = cache
                iStart += k
    
cl = Solution()
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
k = 15
res = cl.rotate(nums, k)
        


















