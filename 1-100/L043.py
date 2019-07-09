# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:29:39 2019

@author: admin
"""

'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

'''


class Solution:
    def multiply(self, num1, num2):
        '''
        num1 : str
        num2 : str
        return : str
        '''
        if num1 == '0':
            return '0'
        
        if num2 == '0':
            return '0'
        
        
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            ni = int(num1[-1 - i])
            for j in range(len(num2)):
                nj = int(num2[-1 - j])
                
                nij = ni * nj
                res[-1 - i -j] += nij


       

        for i in range(len(res)):
            res[-1 - i] = str(res[-1 - i])
            if len(res[-1 - i]) >= 2:
                for j in range(len(res[-1-i]) - 1):
                    idx_fwd = len(res[-1-i]) - j - 1
                    res[-1-i-idx_fwd] += int(res[-1-i][j])

                res[-1 - i] = res[-1-i][j + 1:]

        res = ''.join(res)
        for i in range(len(res)):
            if res[i] != '0':
                res = res[i:]
                break

        return res


cl = Solution()
                
num1 = "999"
num2 = "999"        

res = cl.multiply(num1, num2)
        


