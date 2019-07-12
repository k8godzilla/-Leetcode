# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 09:33:02 2019

@author: admin
"""

'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''



class Solution:
    def climbStairs(self, n):
        # n : int
        # return : int
        
        n0 = math.factorial(n)
        n2 = n0
        n1 = 1
        
        comb = 0
        num_two = 0
        comb += int(n0 / (n1 * n2))
        num_two += 1
        d0 = n
        d2 = n
        while n - 2 * num_two >= 0:


            n1 *= num_two

            n0 //= d0
            d0 -= 1
            n2 //= d2
            d2 -= 1
            try:
                n2 //= d2
                d2 -= 1
            except:
                pass

            comb += int(n0 / (n1 * n2))
            num_two += 1
        return comb
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

