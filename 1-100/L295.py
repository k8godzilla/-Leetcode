# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:13:18 2019

@author: admin
"""

'''
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-median-from-data-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''





class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lows = []
        self.highs = []
        
    def addNum(self, num: int) -> None:
        if len(self.lows) == 0:
            self.lows.append(num)
        elif num <= self.lows[0]:
            self.lows.append(num)
            self.maxHeapifyBottomToTop(self.lows, len(self.lows) - 1)
        else:
            self.highs.append((-1) * num)
            self.maxHeapifyBottomToTop(self.highs, len(self.highs) - 1)
        
        if len(self.lows) - len(self.highs) == 2:
            t = self.lows[0]
            self.lows[0] = self.lows[-1]
            self.lows.pop()
            self.maxHeapifTopToBottom(self.lows, 0)
            self.highs.append((-1) * t)
            self.maxHeapifyBottomToTop(self.highs, len(self.highs) - 1)
        elif len(self.highs) -len(self.lows) == 1:
            t = self.highs[0] * (-1)
            self.highs[0] = self.highs[-1]
            self.highs.pop()
            self.maxHeapifTopToBottom(self.highs, 0)
            self.lows.append(t)
            self.maxHeapifyBottomToTop(self.lows, len(self.lows) - 1)
                        

    def findMedian(self) -> float:
        if len(self.lows) > len(self.highs):
            return self.lows[0]
        else:
            return (self.lows[0] - self.highs[0]) / 2
    
    def maxHeapifyBottomToTop(self, heaps, idx):
        if idx > 0:
            if heaps[idx] > heaps[(idx - 1) // 2]:
                cache = heaps[(idx - 1) // 2]
                heaps[(idx - 1) // 2] = heaps[idx]
                heaps[idx] = cache
                self.maxHeapifyBottomToTop(heaps, (idx - 1) // 2)

    def maxHeapifTopToBottom(self, heaps, idx):
        if 2 * idx + 1 <= len(heaps) - 1:
            left = heaps[2 * idx + 1]
            if 2 * idx + 2 > len(heaps) - 1:
                if left > heaps[idx]:
                    cache = heaps[idx]
                    heaps[idx] = left
                    heaps[2 * idx + 1] = cache
            else:
                right = heaps[2 * idx + 2]
                if left > heaps[idx] and left >= right:
                    cache = heaps[idx]
                    heaps[idx] = left
                    heaps[2 * idx + 1] = cache
                    self.maxHeapifTopToBottom(heaps, 2 * idx + 1)
                elif right > heaps[idx] and right >= left:
                    cache = heaps[idx]
                    heaps[idx] = right
                    heaps[2 * idx + 2] = cache
                    self.maxHeapifTopToBottom(heaps, 2 * idx + 2)
                    
                    
            
            
            
            
import numpy as np
cl = MedianFinder()

nums = np.random.randint(0, 1000, 1000)

for i in range(len(nums)):
    cl.addNum(nums[i])
    print(np.median(nums[:i + 1]))
    print(cl.findMedian())
                
                
                


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()














