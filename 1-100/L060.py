# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:26:39 2019

@author: admin
"""

'''
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        k = k - 1
        if n == 1:
            return '1'
        
        res = ''
        num_pool = list(range(1 + n))
        
        factor = 1
        for i in range(1, n):
            factor *= i
            
        count = 1
        while n >count:
            
            idx = int(k / factor)
            print(n, count, idx)
            k = k % factor
            if n - count > 0:
                factor /= (n - count)
            count += 1
            
            i_count = 0
            for j in range(len(num_pool)):
                if num_pool[j] != 0:
                    if i_count == idx:
                        res += str(num_pool[j])
                        num_pool[j] = 0
                        break
                    else:
                        i_count += 1
                        
        for i in range(len(num_pool)):
            if num_pool[i] != 0:
                res += str(num_pool[i])
                break
                    
        return res
            
cl = Solution()
res= cl.getPermutation(8, 200)
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        











