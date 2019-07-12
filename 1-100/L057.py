# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 09:39:40 2019

@author: admin
"""

'''
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。


'''

class Solution:
    def insert(self, intervals, newInterval):
        # intervals : List[List[int]]
        # newInterval: List[int]
        # return : List[List[int]
        if len(newInterval) == 0:
            return intervals
        if len(intervals) == 0:
            return [newInterval]
        
        # 如果新interval的起点大于原来intervals最后一个intv的重点，就直接把新的加到后面就行        
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        
        start_new, end_new = newInterval
        insert_begin = False #负责标记新intv的插入是否在进行中
        
        res = []
        
        idx = 0
        while idx <= len(intervals) - 1:
            iv_i = intervals[idx]
            start_i, end_i = iv_i
            if insert_begin: # insert正在进行中，处理end_new
                if end_new < start_i: # insert正在进行中，如果end_new小于start_i,并入end_new,再并入当前之后的interval
                    res[-1].append(end_new)
                    res.extend(intervals[idx:])
                    break
                elif end_new <= end_i:  
                    res[-1].append(end_i)
                    res.extend(intervals[idx + 1:])
                    break
            else: # insert 尚未开始， 需要首先判断start_new
                if start_new > end_i:
                    res.append(iv_i)
                else:
                    if end_new < start_i:
                        res.append(newInterval)
                        res.extend(intervals[idx:])
    
                        break
                    elif end_new <= end_i:
                        if start_new < start_i:
                            res.append([start_new, end_i])
                            res.extend(intervals[idx + 1:])
                        else:
                            res.extend(intervals[idx:])
                        break
                    else:
                        res.append([min(start_new, start_i)])
                        insert_begin = True
            idx += 1
        
        ### 到最后如果res的最后一项长度为1，说明end_new还没塞进去
        if len(res[-1]) == 1:
            res[-1].append(end_new)
            
            
        return res
                    

cl = Solution()            
intervals = [[1,3],[6,9]]
newInterval = [2,5]                  

res = cl.insert(intervals, newInterval)
            
            
            
