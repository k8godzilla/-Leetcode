# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:29:09 2019

@author: admin
"""

'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def longestCommonPrefix(self, strs):
        '''
        strs : List[str]
        return : str
        '''
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        res = ''
        idx = 0
        
       
        while True:
            try:
                com_str = strs[0][idx]
            except:
                break
            com = True            
            for i in range(1, len(strs)):
                try:
                    if strs[i][idx] != com_str:
                        com = False
                except:
                    com = False
                if com == False:
                    break
            if com:
                res += com_str
                idx += 1
            else:
                break
        return res
                    
                
 
