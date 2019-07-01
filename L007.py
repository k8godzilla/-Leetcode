# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:32:58 2019

@author: admin
"""

'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def reverse(self, x):
        '''
        x : int
        return : int
        '''
        x_str = str(x)
        x_pre = ''
        idx_start = 0
        if x_str[0] == '-':
            x_pre = '-'
            idx_start += 1
        x_num = ''
        idx_max = len(x_str) - 1
        for i in range(idx_start, len(x_str)):
            x_num += x_str[idx_max - i + idx_start]
        
        idx_non_zero = 0
        while idx_non_zero < len(x_num):
            if x_num[idx_non_zero] != '0':
                break
            idx_non_zero += 1
        
        x_num = x_num[idx_non_zero:]
        if len(x_num) == 0:
            return 0
        else:
            x = int(x_pre + x_num)
            if -2**31<x<2**31-1:
                return x
            else:
                return 0

            
        















