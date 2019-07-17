# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:11:52 2019

@author: admin
"""

'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def partition(self, s: str) -> list:
        # s : str
        # return : List[List[str]]
        if len(s) == 0:
            return []
        
        if len(s) == 1:
            return [[s[0]]]
        
        self.dp = [[s[0], s[1]]]
        if s[0] == s[1]:
            self.dp.append([s[:2]])
            
        for i in range(2, len(s)):
            si = s[i]
            self.dpUpdate(si)
        return self.dp
            
    def dpUpdate(self,si):

        for j in range(len(self.dp)):
            try:
                if self.dp[j][-1] == si:
                    s0 = self.dp[j][:-1]
                    s1 = self.dp[j][-1] + si
                    s0.append(s1)
                    self.dp.append(s0)
                
                if self.dp[j][-2] == si:
                    s0 = self.dp[j][:-2]
                    s1 = ''.join(self.dp[j][-2:])
                    s1 += si
                    s0.append(s1)
                    self.dp.append(s0)
            except:
                pass
            self.dp[j].append(si)
                
            
                
            
        
    

    
    
    
cl = Solution()
   
s = 'dcc'

res = cl.partition(s)    
    
    
    
    
    
    
    
    
    
    
            
            
            
            
            

