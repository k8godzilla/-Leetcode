# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 13:51:36 2019

@author: admin
"""

'''
在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。

每个矩形由其左下顶点和右上顶点坐标表示，如图所示。



示例:

输入: -3, 0, 3, 4, 0, -1, 9, 2
输出: 45

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rectangle-area
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area0 = self.recAreaCompute(A, B, C, D)
        area1 = self.recAreaCompute(E, F, G, H)
        rowOLP = self.overlapCompute(A, C, E, G)
        colOLP = self.overlapCompute(B, D, F, H)
        return area0 + area1 - rowOLP * colOLP
    
    def overlapCompute(self, i0, i1, j0, j1):
        ij0 = max(i0, j0)
        ij1 = min(i1, j1)
        return max(ij1 - ij0, 0)
    
    def recAreaCompute(self, a, b , c, d):
        return (c - a) * (d - b)
    
    
cl = Solution()
res = cl.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)