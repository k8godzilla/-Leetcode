# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:42:40 2019

@author: admin
"""

'''
有一队人（两人或以上）想要在一个地方碰面，他们希望能够最小化他们的总行走距离。

给你一个 2D 网格，其中各个格子内的值要么是 0，要么是 1。

1 表示某个人的家所处的位置。这里，我们将使用 曼哈顿距离 来计算，其中 distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|。

示例：

输入: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

输出: 6 

解析: 给定的三个人分别住在(0,0)，(0,4) 和 (2,2):
     (0,2) 是一个最佳的碰面点，其总行走距离为 2 + 2 + 2 = 6，最小，因此返回 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-meeting-point
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。          
'''


class Solution:
    def minTotalDistance(self, grids: list) -> int:
    # def minTotalDistance(self, grid: List[List[int]]) -> int:
        xIdx, yIdx = [], []
        for i in range(len(grids)):
            for j in range(len(grids)):
                if grids[i][j] == 1:
                    yIdx.append(i)
                    xIdx.append(j)
        xIdx.sort()
        yIdx.sort()
        if len(xIdx) // 2 == 1:
            xMedian = xIdx[(len(xIdx) - 1) // 2]
            yMedian = yIdx[(len(yIdx) - 1) // 2]
        else:
            xMedian = (xIdx[(len(xIdx) - 1) // 2] + xIdx[(len(xIdx) - 0) // 2]) // 2 
            yMedian = (yIdx[(len(xIdx) - 1) // 2] + yIdx[(len(xIdx) - 0) // 2]) // 2 

        dist = 0
        for x in xIdx:
            dist += abs(x - xMedian)
        for y in yIdx:
            dist += abs(y - yMedian)
            
        return dist










