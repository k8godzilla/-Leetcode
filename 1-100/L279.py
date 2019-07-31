# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:12:05 2019

@author: admin
"""

'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def numSquares(self, n: int) -> int:
                
        self.squaresSet = set()
        self.squaresList = []
        nb = 1
        while True:
            nbb = pow(nb, 2)
            self.squaresSet.add(nbb)
            self.squaresList.append(nbb)
            if nbb >= n:
                break
            nb += 1
            
            

        self.frontier = [[n]]
        self.res = n + 1
        while self.frontier != []:
            f = self.frontier.pop()
            if len(f) >= self.res:
                continue
            if f[-1] in self.squaresSet:
                self.res = min(self.res, len(f))
            else:
                for s in self.squaresList:
                    r = f[-1] - s
                    if r > 0:
                        fNew = f[:-1] + [s, r]
                        self.frontier.append(fNew)
                    else:
                        break
        return self.res
        
        
cl = Solution()
res = cl.numSquares(10007)        
        
        
            

