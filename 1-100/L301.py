# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:51:17 2019

@author: admin
"""

'''
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-invalid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def removeInvalidParentheses(self, s: str) -> list:
    # def removeInvalidParentheses(self, s: str) -> List[str]:
        leftSub = []
        left, right = 0, 0
        idx = 0
        idxStart = 0
        while idx < len(s):
            if s[idx] == '(':
                left += 1
            elif s[idx] == ')':
                right += 1
            if right > left:
                leftSub.append(s[idxStart:idx])
                while idx < len(s) and s[idx] == ')' : 
                    idx += 1
                left, right = 0, 0
                idxStart = idx
            else:
                idx += 1
        if left == right:
            leftSub.append(s[idxStart:len(s)])
        return leftSub
    
cl = Solution()
s = "()())()"
            

res = cl.removeInvalidParentheses(s)