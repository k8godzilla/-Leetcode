# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 09:37:34 2019

@author: admin
"""

'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def longestValidParentheses(self, s):
        ### s : str
        ### return : int
        len_max = 0
        while s:
            print('f', s)
            len_submax, s = self.forwardSearch(s)
            len_max = max(len_max, len_submax)
            if s:
                print('b', s)
                len_submax, s = self.backwardSearch(s)
                len_max = max(len_max, len_submax)
        return len_max
            
    def forwardSearch(self, s):
        idx_start = 0
        while idx_start < len(s):
            if s[idx_start] == '(':
                score_left, score_right = 1, 0
                i = len(s) - 1
                idx_mark = 0
                score = 0
                for i in range(idx_start + 1, len(s)):
                    if s[i] == '(':
                        score_left += 1
                    else:
                        score_right += 1
                    if score_right > score_left:
                        return 2 * score_left, s[i + 1:]
                    if score_right == score_left:
                        idx_mark = i
                        score = score_left
                if idx_mark > 0:
                    return 2 * score, s[idx_mark + 1:]
                else:
                    return 0, s[idx_start +  1:]
            else:
                idx_start += 1
        return 0, ''
    
    def backwardSearch(self, s):
        idx_end = len(s) - 1
        while idx_end > 0:
            if s[idx_end] == ')':
                score_left, score_right = 0, 1
                idx_mark = idx_end
                for i in range(idx_end - 1, -1, -1):
                    
                    if s[i] == '(':
                        score_left += 1
                    else:
                        score_right += 1
                    if score_left > score_right:
                        return 2 * score_right, s[:i]
                    if score_right == score_left:
                        idx_mark = i
                        score = score_left
                if idx_mark != idx_end:
                    return 2 * score, s[:idx_mark]
                else:
                    return 0, s[:idx_end]
            else:
                idx_end -= 1
        return 0, ''
            
            


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res1 = 0
        for i in range(n):
  
            if i>0 and s[i] == ")":
                if  s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res1:
                    res1 = dp[i]
            print(i,dp)
        return res1  
    
cl = Solution()
s = "))))())()()(()"
                
res = cl.longestValidParentheses(s)
        
        
    
