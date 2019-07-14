#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 09:58:15 2019

@author: sunyin
"""

class Solution:
    def largestRectangleArea(self, heights):
        # heights : List[int]
        # return : int
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        
        idx_height = [[0, heights[0]]]
        area_max = 0
        for i in range(1,len(heights)):
            # 如果当前height大于前一个 在缓存idx_height中加入当前的idx和height
            if heights[i] > heights[i - 1]:
                idx_height.append([i, heights[i]])
            elif heights[i] < heights[i - 1]:

                # 从后向前更新idx_height
                for j in range(-1, (-1) * len(idx_height) - 1, -1):
                    # 如果存储的height大于height_i
                    # 求一下面积 更新最大面积
                    # 更新idx_height


                    if idx_height[j][1] > heights[i]:
                        
                        area = (i - idx_height[j][0]) * idx_height[j][1]
                        area_max = max(area_max, area)
                        idx_height[j][1] = heights[i]
                    elif idx_height[j][1] < heights[i]:
                        # 如果遇到更小的height 直接弹出
                        break
                # 如果idx_height中后面的height不大于前面的height 删除

                for j in range(len(idx_height) - 1, 0, -1):
                    if idx_height[j][1] <= idx_height[j - 1][1]:
                        del idx_height[j]

        # 遍历之后，以len(heights)为边 再更新一次面积
        for j in range(len(idx_height)):
            area = (len(heights) - idx_height[j][0]) * idx_height[j][1]
            area_max = max(area, area_max)
        return area_max
                

cl = Solution()
heights = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
res = cl.largestRectangleArea(heights)



