#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 09:24:56 2019

@author: sunyin
"""

'''
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        # fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if n == 0:
            return str(0)
        
        if n * d < 0:
            pn = '-'
        else:
            pn = ''
        n = abs(n)
        d = abs(d)
        
        itg = n // d
        res = n % d
        if res == 0:
            return pn + str(itg)
        
        self.decimals = []
        self.residual = {}
        self.residual[res] = 0
        
        idx = 1
        while True:
            res *= 10
            self.decimals.append(str(res // d))
            res = res % d
            if res == 0 or res in self.residual:
                break
            else:
                self.residual[res] = idx
                idx += 1
        
        if res == 0:
            itg = str(itg) + '.'
            dec = ''.join(self.decimals)
            res = itg + dec
            return pn + res
        else:
            idx = self.residual[res]
            itg = str(itg) + '.'
            dec0 = ''.join(self.decimals[:idx])
            dec1 = ''.join(self.decimals[idx:])
            res = itg + dec0 + '(' + dec1 + ')'
            return pn + res
            
            
                
        
        
cl = Solution()
res = cl.fractionToDecimal(-50, 8)
        
        
        