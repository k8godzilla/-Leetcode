# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:27:29 2019

@author: admin
"""

'''
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1: 

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        mBin = bin(m)[2:]
        nBin = bin(n)[2:]
        mnBin = []
        for i in range(-1, -1 * len(mBin) - 1, -1):
            if mBin[i] == '1' and nBin[i] == '1':
                mnBin.append('1')
            else:
                mnBin.append('0')
        mnBin.reverse()
        print(mnBin)
        return int(''.join(mnBin), base = 2)
'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        t=0
        while m!=n:
            m>>=1
            n>>=1
            t+=1
        return n<<t

       
        
cl = Solution()
m, n = 3, 5
res = cl.rangeBitwiseAnd(m, n)
