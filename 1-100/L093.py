#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:56:41 2019

@author: sunyin
"""

'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



class Solution:
    def restoreIpAddresses(self, s):
        # s : str
        # return : List[str]
        return self.ipAnyLength(s, 4)
        
        
        
    def ipAnyLength(self, s, length):
        if len(s) < length:
            return []
        
        # 原来字符串的每一个字符都要用到，所以二位数和三位数不可以以0开头，否则0会消失。
        # 递归4 －3 －2 －1 逐一构建
        if length == 1:
            if len(s) <= 1:
                return [s]
            else:
                if s[0] != '0':
                    if len(s) <= 2:
                        return [s]
                    elif len(s) > 3:
                        return []
                    elif int(s) <= 255:
                        return [str(int(s))]
                    else:
                        return []
                else:
                    return []
                    
        else:
            ip_pool = []
            s0 = str(int(s[0]))
            ip0 = self.ipAnyLength(s[1:], length - 1)
            if ip0:
                for ip in ip0:
                    ip_pool.append(s0 + '.' + ip)
            
            if s[0] != '0':
                s1 = str(int(s[:2]))
      
                ip1 = self.ipAnyLength(s[2:], length - 1)
                if ip1:
                    for ip in ip1:
                        ip_pool.append(s1 + '.' + ip)
            
                
                if int(s[:3]) <= 255:
                    s2 = str(int(s[:3]))
                    ip2 = self.ipAnyLength(s[3:], length - 1)
                    if ip2:
                        for ip in ip2:
                            ip_pool.append(s2 + '.' + ip)
            return ip_pool
            

            
        
        
cl = Solution()
       
s = "010010"

res = cl.restoreIpAddresses(s)











