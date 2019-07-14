#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:18:45 2019

@author: sunyin
"""




class Solution:
    def grayCode(self, n):
        # n : int
        # return List(int)
        
        if  n == 0:
            return [0]
        
        b_code = self.grayCodeBinary(n)
        res = []
        for i in range(0, len(b_code), 2):
            num = self.binaryToInt(b_code[i])
            res.append(num)
            # 省去一半计算幂函数的时间
            if num % 2 == 0:
                res.append(num + 1)
            else:
                res.append(num - 1)

        return res
        
        
    def grayCodeBinary(self, n):
        if n == 0:
            return [[0]]
        # 必要 防止n递归到0 而0的模式和其它数字不同
        if n == 1:
            return [[0], [1]]
        else:
            # 回溯
            # 回溯产生的code相邻之间已经保证相差为1, 所以再加上新的0和1就行了
            # 边界上需要反转上一轮产生的code
            b_old = self.grayCodeBinary(n - 1)
            b_new = []
            for i in range(len(b_old)):
                b_new.append([0] + b_old[i])
            #b_old.reverse()
            for i in range(-1, -1 * len(b_old) - 1, -1):
                b_new.append([1] + b_old[i])
            return b_new

    def binaryToInt(self, b):
        print(b)
        num = 0
        for i in range(-1, (-1) * len(b) - 1, -1):
            if b[i] == 1:

                num += pow(2, abs(i) - 1)
        return num
    

cl = Solution()
res = cl.grayCode(3)