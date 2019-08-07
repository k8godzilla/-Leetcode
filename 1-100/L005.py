# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 17:51:28 2019

@author: admin
"""

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        sNew = '*'
        for i in range(len(s)):
            sNew += s[i]
            sNew += '*'
        
        res = ''
        LR = [0] * len(sNew)
        rightMost = 0
        axis = 0
        for i in range(len(sNew)):
            #print(i, sNew[i], 'res', res)
            if i >= rightMost:
                j, k = i - 1, i + 1
            else:
                iMap = axis - (i - axis)
                rMap = LR[iMap]
                if rMap <= rightMost - i:
                    j, k = i - rMap, i + rMap
                else:
                    j, k = 2 * i - rightMost, rightMost 
                
            while True:
                if j < 0 or k >= len(sNew) or sNew[j] != sNew[k] :
                    k -= 1
                    j += 1
                    break
                else:
                    j -= 1
                    k += 1
            print(i, j, k, sNew[i])
            if k > rightMost:
                rightMost = k
                axis = i
            LR[i] = k - i
            if k - i + 1 > len(res):
                res = sNew[j:k + 1]
        res = res.split('*')
        res = ''.join(res)
        return res
    
cl = Solution()
s = "cbbbbd"
res = cl.longestPalindrome(s)
            
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        

        