#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:12:04 2019

@author: sunyin
"""

'''
中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

写一个函数来计算范围在 [low, high] 之间中心对称数的个数。

示例:

输入: low = "50", high = "100"
输出: 3 
解释: 69，88 和 96 是三个在该范围内的中心对称数
注意:
由于范围可能很大，所以 low 和 high 都用字符串表示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/strobogrammatic-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        
        self.pComb(len(high) - 1)
        self.pp0 = [0, 11, 69, 88, 96]
        self.pp1 = [11, 69, 88, 96]
        self.p0 = [0, 1, 8]
        cHigh, cLow = self.lh(high), self.lh(low)
        i, j = 0, len(low) - 1
        
        cs = True
        while i <= j:
            if i == j:
                if int(low[i] )not in [0, 1, 8]:
                    cs = False
                    break
            else:
                if int(low[i] + low[j]) not in [0, 11, 69, 96, 88]:
                    cs = False
                    break
        
        if cs:
            return cHigh - cLow + 1
        else:
            return cHigh - cLow
    
    
    def pComb(self, length):
        self.p = [3, 4, 12]
        for i in range(3, length + 1):
            self.p.append(self.p[-2] * 5)
            
    def lh(self, s):
        i, j = 0, len(s) - 1
        c = 1
        while i <= j:
            if i == j:
                n = int(s[i])
                for j in range(len(self.p0)):
                    if self.p0[j] > n:
                        break
                c *= j
            else:
                n = int(s[i] + s[j])
                if i == 0:
                    p = self.pp1
                else:
                    p = self.pp0
                for j in range(len(p)):
                    if p[j] > n:
                        break
                c *= j
            i += 1
            j -= 1
        return c + sum(self.p[:len(s) - 1])
        
        
        
cl = Solution()
low = '50'
high = '200'
res = cl.strobogrammaticInRange(low, high)
        
        
            
            