# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:35:46 2019

@author: admin
"""

'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            x = str(x)
            i, j = 0, len(x) - 1
            while i < j:
                if x[i] != x[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True

