# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 13:46:19 2019

@author: admin
"""

'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6


'''


class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        iter_end = False
        sub_max = 0
        sudo = False
        if len(height) <= 2:
            return 0
        else:
            idx = 0
            rain_i = 0
            while idx <= len(height) - 3:
                if iter_end == False:
                    idx, rain_i, iter_end, sub_max = self.look_right(height, idx)
                elif height[idx + 1] <= sub_max:
                    height[idx] = sub_max
                    idx, rain_i, iter_end, sub_max = self.look_right(height, idx)
                else:
                    idx += 1
                rain += rain_i
            return rain
                
                
                    
    def look_right(self, height, idx):
        rain = 0
        sub_max = 0
        status = False
        iter_end = False
        if height[idx] <= height[idx + 1]:
            return idx + 1, 0, iter_end, sub_max
        else:         
            for i in range(idx + 1, len(height)):
                if height[i] > height[i - 1]:
                    status = True
                if status:
                    if height[i] > sub_max:
                        sub_max = height[i]
                if height[idx] <= height[i]:
                    return i, rain, iter_end, sub_max
                else:
                    rain += (height[idx] - height[i])
            iter_end = True
            return idx, 0, iter_end,  sub_max
















