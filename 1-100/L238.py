# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:42:21 2019

@author: admin
"""

'''
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/product-of-array-except-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def productExceptSelf(self, nums: list) -> list:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        i, j = 0, len(nums) - 1
        l, r = 1, 1
        while i < len(nums):
            res[i] *= l
            l *= nums[i]
            res[j] *= r
            r *= nums[j]
            i += 1
            j -= 1
        return res