#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:47:17 2019

@author: sunyin
"""

'''
设计并实现一个 TwoSum 的类，使该类需要支持 add 和 find 的操作。

add 操作 -  对内部数据结构增加一个数。
find 操作 - 寻找内部数据结构中是否存在一对整数，使得两数之和与给定的数相等。

示例 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
示例 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-iii-data-structure-design
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#  注意输入的元素可能重复 所以需要考虑count

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pool = {}
        
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        try:
            self.pool[number] += 1
        except:
            self.pool[number] = 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.pool:
            if value - num in self.pool:
                if num != value - num:
                    return True
                elif self.pool[num] >= 2:
                    return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)