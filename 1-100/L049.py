# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:17:26 2019

@author: admin
"""

'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def groupAnagrams(self, strs):
        # strs: List[str]
        # List[List[str]]
        self.hash_mapping = {}
        self.alpha = 'qwertyuioplkjhgfdsazxcvbnm'  
        self.v = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        for i in range(len(self.v)):
            self.hash_mapping[self.alpha[i]] = self.v[i]
            

        
        mem = {}
        for i in range(len(strs)):
            si = strs[i]
            hi = self.hashCompute(si)
            try:
                mem[hi].append(si)
            except:
                mem[hi] = [si]
                #mem[hi].append([si])
        res = []
        for key in mem:
            res.append(mem[key])
        return res
        
    def hashCompute(self, s):
        v_hash = 1
        for i in range(len(s)):
            v_hash *= self.hash_mapping[s[i]]
        return v_hash
        
        
        
cl = Solution()
strs =["mod","mop","pip","tug","hop","dog","met","zoe","axe","mug","fdr","for","fro","fdr","pap","ray","lop","nth","old","eva","ell","mci","wee","ind","but","all","her","lew","ken","awl","law","rim","zit","did","yam","not","ref","lao","gab","sax","cup","new","job","new","del","gap","win","pot","lam","mgm","yup","hon","khz","sop","has","era","ark"]
res = cl.groupAnagrams(strs)           



       

        