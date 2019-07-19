# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 08:47:11 2019

@author: admin
"""

'''
一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。

为了尽快到达公主，骑士决定每次只向右或向下移动一步。

 

编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。

例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

说明:

骑士的健康点数没有上限。

任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dungeon-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def calculateMinimumHP(self, dungeon: list) -> int:
        # calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        self.dungeon = dungeon
        self.m, self.n = len(dungeon), len(dungeon[0])
        

        
        
        self.dp = [[0] * len(dungeon[0]) for _ in range(len(dungeon))]
        #hp = [[0] * len(dungeon[0]) for _ in range(len(dungeon))]
        
        if self.dungeon[-1][-1] <= 0:
            self.dp[-1][-1] = self.dungeon[-1][-1] 
            
        for i in range(-2, (-1) * self.n - 1, -1):
            v = self.dungeon[-1][i] + self.dp[-1][i + 1]
            if v < 0:
                self.dp[-1][i] = v
        
        for i in range(-2, (-1)*self.m - 1, -1):
            v = self.dungeon[i][-1] + self.dp[i + 1][-1]
            if v < 0:
                self.dp[i][-1] = v
                
        iRow, iCol = self.m - 2, self.n - 2
        while iRow >= 0 and iCol >= 0:
            for j in range(iCol, -1, -1):
                vp = max(self.dp[iRow + 1][j], self.dp[iRow][j + 1])
                v = vp + self.dungeon[iRow][j]
                if v < 0:
                    self.dp[iRow][j] = v
            for i in range(iRow, -1, -1):
                vp = max(self.dp[i][iCol +1], self.dp[i + 1][iCol])
                v = vp + self.dungeon[i][iCol]
                if v < 0:
                    self.dp[i][iCol] = v
            iRow -= 1
            iCol -= 1
        
        
        if self.m >= 2 and self.n >= 2:
            if self.dungeon[0][0] + max(self.dp[0][1], self.dp[1][0]) > 0:
                return 1
            else:
                return abs(self.dungeon[0][0] + max(self.dp[0][1], self.dp[1][0]) - 1)
        elif self.m >= 2:
            if self.dungeon[0][0] + self.dp[1][0] > 0:
                return 1
            else:
                return abs(self.dungeon[0][0] + self.dp[1][0] - 1)
        elif self.n >= 2:
            if self.dungeon[0][0] + self.dp[0][1] > 0:
                return 1
            else:
                return abs(self.dungeon[0][0] + self.dp[0][1] - 1)
        else:
            if self.dungeon[0][0] > 0:
                return 1
            else:
                return abs(self.dungeon[0][0] - 1)
        
        
        
cl = Solution()

import numpy as np

m, n = 10, 1

dg = []
for i in range(m):
    dg.append(np.random.randint(-10, 10, n).tolist())
    

res = cl.calculateMinimumHP(dg)      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        






