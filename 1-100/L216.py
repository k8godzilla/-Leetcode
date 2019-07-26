# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:14:15 2019

@author: admin
"""

'''
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



class Solution:
    def combinationSum3(self, k: int, n: int) -> list:
    # def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        for ns in range(1, 10):
            res.extend(self.combination(ns, k, n))
        return res
    
    
    
    def combination(self, numStart, k, n):
        if 10 - numStart < k:
            return []
        if k * numStart + k * (k - 1) / 2 > n:
            return []
        
        if k == 1:
            if numStart == n:
                return [[numStart]]
            else:
                return []
        
        resSub = []
        for  ns in range(numStart + 1, 10):
            sub = self.combination(ns, k - 1, n - numStart)
            if sub != []:
                resSub.extend(sub)
        if resSub == []:
            return []
        else:
            return [[numStart] + r for r in resSub]
        
        
        
        
cl = Solution()
k = 3
n = 9
res = cl.combinationSum3(k, n)        
        
   
        
        









