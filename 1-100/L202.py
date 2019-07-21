# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:44:32 2019

@author: admin
"""

'''
一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 

输入: 19
输出: true
解释: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        squares = []
        for i in range(10):
            squares.append(i * i)
        
        mem = set()
        mem.add(n)
        nStr = str(n)
        while True:
            nNew = 0
            for i in range(len(nStr)):
                nNew += squares[int(nStr[i])]
            if nNew == 1:
                return True
            if nNew in mem:
                return False
            mem.add(nNew)
            nStr = str(nNew)
            
            
                
                
                
        

