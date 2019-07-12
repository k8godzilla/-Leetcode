# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:05:17 2019

@author: admin
"""

'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


'''


class Solution:
    def generateMatrix(self, n):
        # n : int
        # return : List[List[int]]
        # initialize res with zeros
        res = []
        for i in range(n):
            res.append([0] * n)

        
        # 一圈一圈项里面填
        # 首先设定第一圈的start和end
        start, end = 0, n - 1

        v = 1
        while start < end:
            for i  in range(start, end):
                res[start][i] = v
                v += 1
            for i in range(start, end):
                res[i][end] = v
                v += 1
            for i in range(end, start, -1):
                res[end][i] = v
                v += 1
            for i in range(end, start, -1):
                res[i][start] = v
                v += 1
            # 将圈缩小
            start += 1
            end -= 1
            
        # 如果圈缩成一个点
        if start == end:
            res[start][end] = v
            
        return res


cl = Solution()
res = cl.generateMatrix(10)








