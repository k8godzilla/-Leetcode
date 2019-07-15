#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 21:31:22 2019

@author: sunyin
"""

'''
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/interleaving-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isInterleave(self, s1, s2, s3):

        
        # s1 : str
        # s2 : str
        # s3 : str
        # return : bool
        if len(s3) != len(s1) + len(s2):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if s1[0] == s3[0]:
            if s2[0] != s3[0]:
                return self.isInterleave(s1[1:], s2, s3[1:])
            else:
                # 其它情况都是直来直往 只有在s3[0]既可以匹配s2[0]又可以匹配s1[0]时需要特殊考虑
                # 考虑s1 = ab, s2 = ac, s3 = aabc
                # 此时如果直接分成两个递归 s1 = ab s2 = c s3 = abc 和 s1 = b s2 = ac s3 = abc
                # 会多进行一次递归 因为其实此时因为s3以两个a开始 s1和s2各个以1个a开始 只有一种匹配情况
                # 因此我们首先统计出来 3个字符串中 首字母连续出现的个数
                # 然后对于所有独立组合进行递归 这样可以保证不会有冗余递归
                c1 = self.startRepeat(s1)
                c2 = self.startRepeat(s2)
                c3 = self.startRepeat(s3)
                if c3 > c1 + c2:
                    return False
                res_list = []
                # c 中最少取c3 - c2个首字母 不然不够用 
                for i1 in range(c3 - c2, min(c1, c3) + 1):
                    res_list.append(self.isInterleave(s1[i1:],s2[c3 - i1:], s3[c3:]))
                return any(res_list)
        elif s2[0] == s3[0]:
            return self.isInterleave(s1, s2[1:], s3[1:])
        else:
            return False
        
    def startRepeat(self, s):
        if len(s) == 1:
            return 1
        to_end = True
        for i in range(1, len(s)):
            if s[i] != s[0]:
                to_end = False
                break
        c = i
        if to_end:
            c += 1
        return c
        
            
        
cl = Solution()


#s1 = "abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb"
#s2 = "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc"
#s3 = "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"

s1 ="aa"
s2 ="ab"
s3 ="aaab"


res = cl.isInterleave(s1, s2, s3)


