# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:47:04 2019

@author: admin
"""

'''
给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。

你可以假定该序列中的数都是不相同的。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [5,2,6,1,3]
输出: false
示例 2：

输入: [5,2,1,3,6]
输出: true
进阶挑战：

您能否使用恒定的空间复杂度来完成此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def verifyPreorder(self, preorder: list) -> bool:
    # def verifyPreorder(self, preorder: List[int]) -> bool:
        if len(preorder) <= 1:
            return True
        crit = pow(-2, 31)
        caches = []
        for i in range(1,len(preorder)):
            if preorder[i] < preorder[i - 1]:
                if preorder[i] < crit:
                    return False
                else:
                    caches.append(preorder[i - 1])
            else:
                length = len(caches)
                crit = preorder[i - 1]
                for j in range(length - 1, -1, -1):
                    if caches[j] > preorder[i]:
                        break
                    else:
                        crit = caches.pop()
        return True
                

cl = Solution()
p = [5,2,6,1,3]               
res = cl.verifyPreorder(p)            
            
            
        














