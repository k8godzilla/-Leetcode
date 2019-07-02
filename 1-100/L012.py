# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:20:42 2019

@author: admin
"""

'''
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:

输入: 3
输出: "III"
示例 2:

输入: 4
输出: "IV"
示例 3:

输入: 9
输出: "IX"
示例 4:

输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
示例 5:

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.

'''

class Solution:
    def intToRoman(self, num):
        '''
        num : int
        return : str
        '''
        th_digits= num // 1000
        num = num - th_digits * 1000
        hund_digits = num // 100
        num = num - hund_digits * 100
        ten_digits = num // 10
        digits = num - ten_digits *  10
        
        self.rome = ''
        self.rome += 'M' * th_digits
        

        self.fill('C', 'D', 'M',  hund_digits)
        self.fill('X', 'L', 'C',  ten_digits)
        self.fill('I', 'V', 'X', digits)
        return self.rome
        
        
        
        
    def fill(self, one, five, ten, digit):
        if digit <= 3:
            self.rome += one * digit
        elif digit == 4:
            self.rome += (one + five)
        elif digit <= 8:
            self.rome += five
            self.rome += one * (digit - 5)
        else:
            self.rome += (one + ten)
        
        
        
cl = Solution()
rome = cl.intToRoman(58)       

        
        
        
        


