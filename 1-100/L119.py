# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:46:21 2019

@author: admin
"""

'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def getRow(self, rowIndex):
        # rowIndex : int
        # return : List[int]

        res = []
        for i in range(rowIndex + 1):
            res = self.generateNextRow(res)

        return res

    def generateNextRow(self, last_row):
        if len(last_row) == 0:
            return [1]
        elif len(last_row) == 1:
            return [1, 1]
        else:
            # 没有必要把完整的一行都生成出来 因为每一行都是对称的
            # 只把前一半生成出来就行了
            count = (len(last_row) + 2) // 2
            next_row = [1]
            for i  in range(1,count):
                next_row.append(last_row[i - 1] + last_row[i])
            len_second = len(last_row) + 1 - count
            for i in range(len_second - 1, -1, -1):
                next_row.append(next_row[i])
            return next_row
