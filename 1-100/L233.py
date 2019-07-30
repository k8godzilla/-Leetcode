# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:43:58 2019

@author: admin
"""

'''
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例:

输入: 13
输出: 6 
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-digit-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def countDigitOne(self, n: int) -> int:
        '''
        if n == 0:
            return 0
        elif n < 10:
            return 1
        '''
        if n < 0:
            return 0
        
        nStr = str(n)
        length = len(nStr)
        self.cache = {}
        c = 1
        for i in range(length - 1):
            self.cache[i] = c
            c = 10 * c + pow(10, i + 1)
              
        return self.helper(nStr)
    
    def helper(self, nStr):
        l = len(nStr)
        if l == 1:
            return int(int(nStr) >= 1)
        
        n0 = nStr[0]
        if n0 == '1':
            return int(nStr[1:]) + 1 + self.helper(nStr[1:]) + self.cache[len(nStr) - 2]
        if n0 == '0':
            return self.helper(nStr[1:])
        else:
            return pow(10, l - 1) + (int(n0)) * self.cache[l - 2] + self.helper(nStr[1:])


cl = Solution()


n = 13

res = cl.countDigitOne(n)        

cache = cl.cache


resCheck = 0
for i in range(n + 1):
    si = str(i)
    for j in range(len(si)):
        if '1' == si[j]:
            resCheck += 1




    



