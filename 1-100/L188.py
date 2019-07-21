# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:05:39 2019

@author: admin
"""

'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def maxProfit(self, k: int, prices: list) -> int:
        # maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        else:
            self.dp = [[0] * (len(prices) + 1)]
        
       
        if k <= len(prices) // 2:
            for i in range(k):
                p = self.dp[ -1][0] - prices[0]
                dpNew = [0] * (len(prices) + 1)
                for j in range(2, len(self.dp[0])):
                    p = max(p, self.dp[-1][j -2] - prices[j - 2])
                    dpNew[j] = max(dpNew[j - 1], p + prices[j -1])
                self.dp = self.dp[-2:]
                self.dp.append(dpNew)
            
            return self.dp[-1][-1]
        else:
            res = 0
            for i in range(len(prices) - 1):
                if prices[i + 1] > prices[i]:
                    res += prices[i + 1] - prices[i]
            
            return res


    
cl = Solution()
prices = [1, 2, 4]
k = 2
res = cl.maxProfit(k, prices)

dp = cl.dp










