# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:05:43 2019

@author: admin
"""

'''
你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：

-1 表示墙或是障碍物
0 表示一扇门
INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。

示例：

给定二维网格：

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
运行完你的函数后，该网格应该变成：

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/walls-and-gates
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



class Solution:
    def wallsAndGates(self, rooms: list) -> None:
        #  wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        self.walls = set()
        self.roomsInf = set()
        self.doors = set()
        self.explored = set()
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    self.doors.add((i, j))
                elif rooms[i][j] == -1:
                    self.walls.add((i, j))
                else:
                    self.roomsInf.add((i, j))
                    
        front = self.findFrontNext(self.doors)
        while len(front) != 0:
            for f in front:
                dMin = self.findMinDist(f, rooms)
                rooms[f[0]][f[1]] = dMin + 1
                self.explored.add(f)
            front = self.findFrontNext(front)
            
    def findMinDist(self, f, rooms):
        i, j = f
        validN = []
        if (i - 1, j) in self.roomsInf or (i - 1, j) in self.doors:
            validN.append((i - 1, j))
        if (i + 1, j) in self.roomsInf or (i + 1, j) in self.doors:
            validN.append((i + 1, j))
        if (i, j - 1) in self.roomsInf or (i, j - 1) in self.doors:
            validN.append((i, j - 1))
        if (i, j + 1) in self.roomsInf or (i, j + 1) in self.doors:
            validN.append((i, j + 1))
        return min([rooms[idx[0]][idx[1]] for idx in validN])
                    
    def findFrontNext(self, front):
        frontNext = set()
        for f in front:
            i, j = f
            if (i - 1, j) in self.roomsInf and (i - 1, j) not in self.explored:
                frontNext.add((i - 1, j))
            if (i + 1, j) in self.roomsInf and (i + 1, j) not in self.explored:
                frontNext.add((i + 1, j))
            if (i, j - 1) in self.roomsInf and (i, j - 1) not in self.explored:
                frontNext.add((i, j - 1))
            if (i, j + 1) in self.roomsInf and (i, j + 1) not in self.explored:
                frontNext.add((i, j + 1))
        return frontNext
            
                    
                    
                    
                    
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        