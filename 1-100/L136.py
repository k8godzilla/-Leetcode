# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:15:00 2019

@author: admin
"""

'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
 
class Solution:
    def singleNumber(self, nums: list) -> int:
        # singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
            idx = abs(round(nums[i])) % len(nums)
            nums[idx] += 0.01
        

        for i in range(len(nums)):

            if round((nums[i] * 100) % 2) == 1:
                resid0 = i
                break
   
        for i in range(len(nums)):
            nums[i] = round(nums[i])
            
        for i in range(len(nums)):
            idx = abs(round(nums[i])) % (len(nums) + 1)
            nums[idx] += 0.01
        
        for i in range(len(nums)):
            if round((nums[i] * 100) % 2) == 1:
                resid1 = i
                break

        
        
        for i in range(len(nums)):
            nums[i] = round(nums[i])
            
        for i in range(len(nums)):
            idx = abs(round(nums[i] + 1)) % (len(nums))
            nums[idx] += 0.01
            
        for i in range(len(nums)):
            if round((nums[i] * 100) % 2) == 1:
                resid2 = i
                break
        '''
        for i in range(len(nums)):
            nums[i] = round(nums[i])
        '''


        for i in range(len(nums)):
            if abs(round(nums[i])) % len(nums) == resid0:
                if abs(round(nums[i])) % (len(nums) + 1) == resid1:
                    if abs(round(nums[i] + 1)) % (len(nums)) == resid2:
                        return round(nums[i])
  
        
                
            
cl = Solution()
nums = [-1,-1,-2]
res = cl.singleNumber(nums)      
            

