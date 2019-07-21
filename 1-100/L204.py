# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 18:39:23 2019

@author: admin
"""

'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [True] * n
        count = 0
        for i in range(2, n):
            if primes[i]:
                count += 1
                for j in range(2 * i, n, i):
                    primes[j] = False
        return count
    

cl = Solution()
res = cl.countPrimes(10)