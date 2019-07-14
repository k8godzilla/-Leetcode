#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:55:39 2019

@author: sunyin
"""


'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
        
        # 预存所有可能code
        codes = set()
        for i in range(1, 27):
            codes.add(str(i))
        
        # 使用dp来存储每一个长度的可能数目
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            # 0因为本身无法编码, 所以可能会造成无法编码的情况
            # 0因为本身无法编码所以需要特殊处理
            if s[i] == '0':
                if s[i - 1:i + 1] not in  codes:
                    return 0
                if i < 2:
                    dp[i] = 1
                else:
                    dp[i] = dp[i - 2]
            else:
                if s[i-1:i + 1] in codes:
                    if i < 2:
                        dp[i] = 2
                    else:
                        # 实际的式子是 dp[i] = 2 * (dp[i - 2]) + (dp[i - 1] - dp[i - 2])
                        dp[i] =  dp[i - 2] + dp[i - 1] 
                else:
                    dp[i] = dp[i - 1]
        return dp[-1]
        