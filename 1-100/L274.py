# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 09:43:32 2019

@author: admin
"""

'''
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。

h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）至少有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）”

 

示例:

输入: citations = [3,0,6,1,5]
输出: 3 
解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。
 

说明: 如果 h 有多种可能的值，h 指数是其中最大的那个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/h-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def hIndex(self, cit) -> int:
        if cit == []:
            return 0
        
        hs = []
        for i in range(len(cit)):
            if cit[i] > len(hs):
                hs.append(cit[i])
                if hs[0] < len(hs):
                    hs = hs[1:]
                hs.sort()
        return len(hs)
        



cl = Solution()
c = [4,1,2,7,5,3,1]
res = cl.hIndex(c)










