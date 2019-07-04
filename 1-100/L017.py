# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:17:36 2019

@author: admin
"""

'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def letterCombinations(self, digits):
        '''
        digits : str
        return List[str]
        '''
        if len(digits) == 0:
            return []
        self.dsm = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        
        res = list(self.dsm[digits[0]])
        if len(digits) == 1:
            return res
        else:
            for i in range(1, len(digits)):
                res = self.comb_update(res, digits[i])
            return res
    
    def comb_update(self, res, dg):
        res_new = []
        for ab in self.dsm[dg]:
            for r in res:
                res_new.append(r + ab)
        return res_new
        
        
        
