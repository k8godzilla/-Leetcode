#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 08:10:39 2019

@author: sunyin
"""

class Solution:
    def getFactors(self, n: int):
        self.mem = {}
        
        
        return self.helper(n)
          
    def helper(self,  n):
        try:
            return self.mem[n]
        except:
            res = []
            d = 2
            while d <= n // d:
                if n % d == 0:
                    res.append([d, n // d])
                    fd = self.helper(n // d)
                    for f in fd:
                        if d <= f[0]:
                            f = [d] + f
                            res.append(f)
                d += 1
            self.mem[n] = res
            return res
        
        
        
    
    
cl = Solution()
n = 12

f = cl.getFactors(n)