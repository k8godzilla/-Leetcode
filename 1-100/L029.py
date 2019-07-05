# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:54:37 2019

@author: admin
"""

'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # dividend : int
        # divisor : int
        # return : int
        
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            mark = 1
        else:
            mark = -1
            
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor: return 0
        
        ### power locate
        dvs_power = [divisor]

        while True:
            dvs_next = dvs_power[-1] + dvs_power[-1]
            if dvs_next > dividend:
                break
            else:
                dvs_power.append(dvs_next)
            if len(dvs_power) > 31:
                if mark == 1:
                    return pow(2,31) - 1
                else:
                    return pow((-2), 31)
        
        res = 0
        i = len(dvs_power) - 1
        cum = 0
        while i >=0:
            if cum + dvs_power[i] <= dividend:
                res += pow(2, i)
                cum += dvs_power[i]
            i -= 1
            if cum == dividend:
                break
        return res * mark
            
            
            






