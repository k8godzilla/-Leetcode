#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:29:43 2019

@author: sunyin
"""

'''
验证给定的字符串是否可以解释为十进制数字。

例如:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：

数字 0-9
指数 - "e"
正/负号 - "+"/"-"
小数点 - "."
当然，在输入中，这些字符的上下文也很重要。


'''


class Solution:
    def isNumber(self, s):
        # s : str
        # return : bool
        
        if len(s) == 0:
            return False
        nums = '1234567890'
     
        
        s_g = {}
        for i in range(len(nums)):
            s_g[nums[i]] = 'n'
        s_g['e'] = 'e'
        s_g['+'] = 'pn'
        s_g['-'] = 'pn'
        s_g['.'] = 'f'
        s_g[' '] = 'sp'
        
        g_a = {}
        g_a['n'] = True
        g_a['e'] = False
        g_a['pn'] = True
        g_a['f'] = True
        g_a['sp'] = True
        
    
        num_app = False
        f_app = False
        
        for i in range(len(s)):

            try:
                g = s_g[s[i]]
                a = g_a[g]
                if a == False:
                    return False
                elif g == 'f':
                    del s_g['.']
                    f_app = True
                    try:
                        if s_g[s[i + 1]] == 'pn':
                            return False
                    except:
                        pass
   
                elif g == 'pn':
                    del s_g['+']
                    del s_g['-']
                    if i + 1 == len(s):
                        return False
                    if s[i + 1] == ' ':
                        return False
                elif g == 'n':
                    num_app = True
                    g_a['f'] = True
                    g_a['e'] = True
                    g_a['pn'] = False
                elif g == 'e':
                    if i + 1 == len(s):
                        return False
                    if s[i + 1] == ' ':
                        return False
                    s_g['+'] = 'pn'
                    s_g['-'] = 'pn'
                    g_a['pn'] = True
                    del s_g['e']
                    try:
                        del s_g['.']
                    except:
                        pass
                elif g == 'sp':
                    if num_app or f_app:
                        del s_g
                        s_g = {}
                        s_g[' '] = 'sp'
            except:
                return False
        
        return num_app



cl = Solution()

res = cl.isNumber(".1" )

'''
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
'''

" "




