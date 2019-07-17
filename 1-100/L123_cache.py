#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 20:28:19 2019

@author: sunyin
"""


class Solution():
    def maxProfit(self, prices):
        if not prices: return 0
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):
            pre_max = -prices[0]
            for i in range(1, n):
                pre_max = max(pre_max, dp[k - 1][i - 1] - prices[i])
                print(k,i,pre_max)
                dp[k][i] = max(dp[k][i - 1], prices[i] + pre_max)
                print(dp)
        return dp[-1][-1]



cl = Solution()

prices = [1, 2, 0, 4]

res_cache = cl.maxProfit(prices)






price_debug0 = dp[-1]