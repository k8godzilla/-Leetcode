# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 14:16:13 2019

@author: admin
"""

'''
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def calculate(self, s: str) -> int:
        s.replace(' ','')
        idxC = [i for i in range(len(s)) if s[i] in '+-*/']
        
        if len(idxC) == 0:
            return int(s)
        
        c = [s[i] for i in idxC]
        idxC = [-1] + idxC + [len(s)]
        nums = [int(s[idxC[i] + 1:idxC[i + 1]]) for i in range(len(idxC) - 1)]
        
        idx = 0
        res = 0
        while idx < len(nums):
            m, idx = self.mdCompute(nums, c, idx)
            res += m
    
        
        return res
    
    def mdCompute(self, nums, c, idx):
        if idx == 0:
            t = 1
        else:
            if c[idx - 1] == '+':
                t = 1
            else:
                t = -1
        
        m = nums[idx]
        while idx < len(c):
            if c[idx] == '*':
                m *= nums[idx + 1]
            elif c[idx] == '/':
                m //= nums[idx + 1]
            else:
                break
            idx += 1
        return m * t, idx + 1
                
                
                
                
                
        
        
        
        
        

cl = Solution()
a = "3+2*2"

res = cl.calculate(a)

