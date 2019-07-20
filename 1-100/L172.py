#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:03:10 2019

@author: sunyin
"""

'''
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''




class Solution:
    def trailingZeroes(self, n: int) -> int:
        ns = str(n)
        if len(ns) == 1:
            return (n + 5) // 10
        else:
            '''
            a = []
           
            for i in range(1,len(ns)):
                a.append(int(ns[:i]) - sum(a))
               
            

            p = len(ns) - 1
            zeros = 0
            for i in range(len(a)):
                zeros += a[i] * p
                p -= 1
            '''
            import math
            fives = self.countFive(n)
 
            return fives
        
    def countFive(self, n):

        if n < 5:
            return 0
        powFive = int(math.log(n) / math.log(5))
        p5 =  pow(5, powFive)
        res = n % p5
        t = n // p5
        

        c5 = 0
        for i in range(powFive):
            c5 += pow(4, i) * (powFive - i)
        c5 *= t
        
        return c5 + self.countFive(res)
            
            



        
    
cl = Solution()
res = cl.trailingZeroes(202)
        

            
f = cl.countFive(100)           
            
            
                
        
