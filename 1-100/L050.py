# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:56:30 2019

@author: admin
"""

'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。


'''

class Solution:
    def myPow(self, x, n):
        ### x : float
        ### n : int
        ### return : float
        
        neg = False
        if n < 0:
            n = (-1) * n
            neg = True
        
        v_list = [x]
        p_list = [1]
        p = 1
        while p <= n:
            v_list.append(v_list[-1] * v_list[-1])
            p_list.append(2 * p_list[-1])
            p += p_list[-1]
            
        v = 1
        idx = -1
        p = 0
        while p < n:
            if p + p_list[idx] == n:
                v *= v_list[idx]
                break
            elif p + p_list[idx] < n:
                p += p_list[idx]
                v *= v_list[idx]
            idx -= 1
        if neg:
            return 1/v
        return v
                
            
cl = Solution()
res = cl.myPow(2, -2)            
            
            
            
            
            
            
            
            
            
            
            
        
        
