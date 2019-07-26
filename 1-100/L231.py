# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:02:27 2019

@author: admin
"""

'''
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 2^0 = 1
示例 2:

输入: 16
输出: true
解释: 2^4 = 16
示例 3:

输入: 218
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        pool = set()
        start = 1
        for i in range(12):
            pool.add(start)
            start *= 2
        
        nLen = len(str(n))
        powStart = pow(2, (nLen - 1) * 3)
        
        if n % powStart != 0:
            return False
        
        if n // powStart not in pool:
            return False
        
        return True
            
        
        
        
        
        





