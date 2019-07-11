#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 08:53:04 2019

@author: sunyin
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        elif len(intervals) == 1:
            return intervals
        
        ### 录入所有的起点和终点并排序
        starts, ends = [], []
        for i in range(len(intervals)):
            starts.append(intervals[i][0])
            ends.append(intervals[i][1])
            
        starts.sort()
        ends.sort()
        
        # 双指针p_start, p_end从前向后滑动
        # 当划过一个start时 se_mem -= 1,滑过一个end时，se_mem += 1
        # 当划过一个start时如果se_mem = 0, 则开始一个新的子interval
        # 当划过一个end时如果se_mem = -1, 则完成一个interval
        # 滑动时，优先选择start就可以处理好start ＝ end的情况
        se_mem = 0 
        res = []
        p_start, p_end = 0, 0
        while p_start < len(starts) and p_end < len(ends):
            if starts[p_start] <= ends[p_end]:
                if se_mem == 0:
                    res_sub = [starts[p_start]]
                se_mem -= 1
                p_start += 1
            else:
                if se_mem == -1:
                    res_sub.append(ends[p_end])
                    res.append(res_sub)
                se_mem += 1
                p_end += 1
        #如果滑动完了，res_sub只有一个起点，则吧最后的end塞进去       
        if len(res_sub) == 1:
            res_sub.append(ends[-1])
            res.append(res_sub)
        return res
                