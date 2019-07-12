# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:02:25 2019

@author: admin
"""

'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？



例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28

'''

### 就是一个组合问题而已
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m = m - 1
        n = n - 1
        if m == 0 or n == 0:
            return 1
        else:

            res = 1
            num_min, num_max = min(m, n), max(m, n)
            for i in range(1, num_min + 1):
                res *= (num_max + i)
                res /= i
                
            return int(res)
