#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 11:51:52 2019

@author: sunyin
"""

'''
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:

输入: "2-1-1"
输出: [0, 2]
解释: 
((2-1)-1) = 0 
(2-(1-1)) = 2
示例 2:

输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/different-ways-to-add-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def diffWaysToCompute(self, s: str) -> list:
        # diffWaysToCompute(self, s: str) -> List[int]:
        self.nums, self.cp = [], []
        self.cpPool = '+-*'
        m = 0
        for i in range(len(s)):
            if s[i] in self.cpPool:
                self.nums.append(int(s[m:i]))
                self.cp.append(s[i])
                m = i + 1
        self.nums.append(int(s[m:]))
        
        if len(self.cp) == 0:
            return self.nums
        
        # wash *, * is washed out if its left and right are also *
        f = [0]
        for i in range(1,len(self.cp) - 1):
            if self.cp[i] == '*' and self.cp[i - 1] == '*' and self.cp[i + 1] == '*':
                f.append(1)
            else:
                f.append(0)
        if len(self.cp) > 1:
            f.append(0)
            
        n, c = [], []
        t = 1
        for i in range(len(f)):
            if f[i] == 0:
                n.append(self.nums[i] * t)
                c.append(self.cp[i])
                t = 1
            else:
                t *= self.nums[i]
        n.append(self.nums[-1])
        
        self.nums, self.cp = n, c
        
        f = [0]
        for i in range(1, len(self.cp) - 1):
            if self.cp[i] == '-' and self.cp[i - 1] == '+' and self.cp[i+1] == '+':
                f.append(1)
            else:
                f.append(0)
        if len(self.cp) > 1:
            f.append(0)
            
        n, c = [], []
        for i in range(len(f)):
            if f[i] == 0  and f[i - 1] != 1:
                n.append(self.nums[i])
                c.append(self.cp[i])
            if f[i] == 1:
                n.append(self.nums[i] - self.nums[i+1])
                c.append('+')
        n.append(self.nums[-1])
         
        
        self.nums, self.cp = n, c
        f = [0]
        for i in range(1, len(self.cp) - 1):
            if self.cp[i] == '+' and self.cp[i - 1] == '+' and self.cp[i+1] == '+':
                f.append(1)
            else:
                f.append(0)
        if len(self.cp) > 1:
            f.append(0)
            
        n, c = [], []
        t = 0
        for i in range(len(f)):
            if f[i] == 0:
                n.append(self.nums[i] + t)
                c.append(self.cp[i])
                t = 0
            if f[i] == 1:
                t += self.nums[i]
        n.append(self.nums[-1])
        
         

        self.result = []
        
        self.frontier = {(n, c)}
        while self.frontier != []:
            n, c = self.frontier.pop()
            if len(c) == 1:
                self.result.append(self.helper(n[0], n[1], c[0]))
            else:
                for i in range(len(c)):
                    nc = self.helper(n[i], n[i+1], c[i])
                    nNew = n[:i] + [nc] + n[i+2:]
                    cNew = c[:i] + c[i+1:]
                    self.frontier.add((nNew, cNew))
                    
                
        
           
        return self.result
    
    def helper(self, n1, n2, cp):
        return eval(str(n1) + cp + str(n2))
    
    
    
        
s = "2*3-4*5"
cl = Solution()
res = cl.diffWaysToCompute(s)
        


 
        
        
        
        
        
        
            

