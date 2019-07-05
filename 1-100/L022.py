# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 14:29:34 2019

@author: admin
"""

'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''


class Solution:
    def generateParenthesis(self, n):
        '''
        n : int
        reteurn: List[str]
        '''
        p0 = ['']
        paren_total = [p0]
        while len(paren_total) <= n:
            self.parenUpdate(paren_total)
        return paren_total[-1]
    
    def parenUpdate(self, paren_total):
        p_next = []
        i, j = 0, len(paren_total) - 1
        while i <= j:
            p_next.extend(self.groupMerge(paren_total[i], paren_total[j]))
            i += 1
            j -= 1
        paren_total.append(list(set(p_next)))
        return paren_total
        
    
    def groupMerge(self, paren_m, paren_n):
        m = []
        for pm in paren_m:
            for pn in paren_n:
                m.append(self.parenGenerate(pm,pn))
                m.append(self.parenGenerate(pn, pm))
        return m
        
    
    def parenGenerate(self, a, b):
        return '(' + a + ')' + b
        
        




