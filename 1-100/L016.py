# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:30:10 2019

@author: admin
"""

'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def threeSumClosest(self, nums, target):
        '''
        nums : List[int],
        target : int
        return : int
        '''
        nums.sort()
        k = 0
        res = abs(nums[0] + nums[1] + nums[2] - target)
        res_sum = nums[0] + nums[1] + nums[2]
        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]: continue # skip.
            i, j = k + 1, len(nums) - 1
            step = 50
            status = 0
            if j - i > 2 * step:
            
                while j - i > step:
    
                    s = nums[k] + nums[i] + nums[j] - target
                    if s < 0:
                        if status == 1:
                            j += step
                            status = 0
                            break
                        else:
                            i += step
                            status = -1
                    elif s > 0:
                        if status == -1:
                            i -= step
                            status = 0
                            break
                        else:
                            j -= step
                            status = 1
                    else:
                        return target


            if status == 1:
                j += step
            elif status == -1:
                i -= step
            
         

            while i < j:
                s = nums[k] + nums[i] + nums[j] - target
                if abs(s) < res:
                    res = abs(s)
                    res_sum = s + target

                
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    return target
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res_sum
        



cl = Solution()

import numpy as np
nums = [-1,2,1,-4]
target = 1

res = cl.threeSumClosest(nums, target)
