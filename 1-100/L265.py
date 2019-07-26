# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:49:47 2019

@author: admin
"""

'''
假如有一排房子，共 n 个，每个房子可以被粉刷成 k 种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x k 的矩阵来表示的。

例如，costs[0][0] 表示第 0 号房子粉刷成 0 号颜色的成本花费；costs[1][2] 表示第 1 号房子粉刷成 2 号颜色的成本花费，以此类推。请你计算出粉刷完所有房子最少的花费成本。

注意：

所有花费均为正整数。

示例：

输入: [[1,5,3],[2,9,4]]
输出: 5
解释: 将 0 号房子粉刷成 0 号颜色，1 号房子粉刷成 2 号颜色。最少花费: 1 + 4 = 5; 
     或者将 0 号房子粉刷成 2 号颜色，1 号房子粉刷成 0 号颜色。最少花费: 3 + 2 = 5. 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/paint-house-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def minCostII(self, costs: list) -> int:
        # minCostII(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        if len(costs[0]) == 0:
            return 0
         
        m, n = len(costs), len(costs[0])
        
        if m == 1:
            return min(costs[0])
        
        for i in range(1, m):
            minGlobal = min(costs[i -1])
            idxSort = sorted(range(n), key = lambda k: costs[i -1][k])
            minSub = min([costs[i - 1][idxSort[j]] for j in range(1, n)])
            for j in range(n):
                if j == idxSort[0]:
                    costs[i][j] += minSub
                else:
                    costs[i][j] += minGlobal
        return min(costs[-1])
        
        
        
        


cl = Solution()

costs = [[1,5,3],[2,9,4]]

res = cl.minCostII(costs)
        
        
        
        


