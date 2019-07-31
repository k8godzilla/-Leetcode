# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:50:57 2019

@author: admin
"""

'''
给出两个一维的向量，请你实现一个迭代器，交替返回它们中间的元素。

示例:

输入:
v1 = [1,2]
v2 = [3,4,5,6] 

输出: [1,3,2,4,5,6]

解析: 通过连续调用 next 函数直到 hasNext 函数返回 false，
     next 函数返回值的次序应依次为: [1,3,2,4,5,6]。
拓展：假如给你 k 个一维向量呢？你的代码在这种情况下的扩展性又会如何呢?

拓展声明：
 “锯齿” 顺序对于 k > 2 的情况定义可能会有些歧义。所以，假如你觉得 “锯齿” 这个表述不妥，也可以认为这是一种 “循环”。例如：

输入:
[1,2,3]
[4,5,6,7]
[8,9]

输出: [1,4,8,2,5,9,3,6,7].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v = [v1, v2]
        self.vLen = [len(self.v[i]) for i in range(len(self.v))]
        self.totalLen = sum(self.vLen)
        self.groupPointer = 0
        self.nPointer = 0
        self.vPointer = [0] * len(self.v)
        
        

    def next(self):
        """
        :rtype: int
        """
        
        while True:
            try:
                res = self.v[self.groupPointer][self.vPointer[self.groupPointer]]
                self.vPointer[self.groupPointer] += 1
                self.nPointer += 1
                self.groupPointer += 1
                if self.groupPointer >= len(self.v):
                    self.groupPointer = 0
                break
            except:
                self.groupPointer += 1
                if self.groupPointer >= len(self.v):
                    self.groupPointer = 0
        return res
            

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.nPointer >= self.totalLen:
            return False
        else:
            return True
        
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

















