# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:24:30 2019

@author: admin
"""

'''
编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 6:
            return n
        
        self.ugly = set(list(range(1, 7)))
        self.beauty = set()
        count = 6
        num = 8
        
        while True:
            if self.numberClean(num):
                self.ugly.add(num)
                count += 1
                if count == n:
                    return num
            else:
                self.beauty.add(num)
            num += 1
         
        
        
        
    
    def numberClean(self, num):
        print(num, len(self.ugly))
        while num >= 0:
            if num % 2 == 0:
                num = num / 2
            else:
                break
            if num in self.ugly:
                return True
            if num in self.beauty:
                return False
        
        while num >= 0:
            if num % 3 == 0:
                num = num / 3
            else:
                break
            if num in self.ugly:
                return True
            if num in self.beauty:
                return False
            
        while num >= 0:
            if num % 5 == 0:
                num = num / 5
            else:
                break
            if num in self.ugly:
                return True
            if num in self.beauty:
                return False
        
        if num > 0:
            return False
        else:
            return True


cl = Solution()

res = cl.nthUglyNumber(12)