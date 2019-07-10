# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:16:15 2019

@author: admin
"""

class Solution:
    def solveNQueens(self, n):
        # n: int
        # return : List[List[str]]
        self.n = n
        self.status = []
        for i in range(n):
            self.status.append([1] * n)
        
        self.solution_total = []
        
        self.solution = []
        
        self.queenPlace(0)
        
        
        return len(self.solution_total)
        
    def queenPlace(self, row):
        for i in range(self.n):
            if self.status[row][i] == 1:
                self.solution.append(i)
                if len(self.solution) == self.n:
                    sol = []
                    for i in range(self.n):
                        sol.append(self.solution[i])
                    if sol == [0, 4, 1, 3, 0]:
                        print(self.status)
                    self.solution_total.append(sol)
                    #self.solution.pop()
                    #return False
                else:
                    grid_cut = self.cutStatus(row, i)
                    #self.cut_cache.append(grid_cut)
                    self.queenPlace(row + 1)
                    self.recoverStatus(grid_cut)
                self.solution.pop()
                
                    
    def recoverStatus(self, grid_cut):
        for i in range(len(grid_cut)):
            j, k = grid_cut[i]
            self.status[j][k] -= 1
                
    def cutStatus(self, row, i):
        grid_cut = []
        for j in range(row + 1, self.n):
            self.status[j][i] += 1
            grid_cut.append((j, i))
        
        k, l = row + 1, i + 1
        while k < self.n and l < self.n:
            self.status[k][l] += 1
            grid_cut.append((k, l))
            k += 1
            l += 1
        
        k, l = row + 1, i - 1
        while k < self.n and l >= 0:
            self.status[k][l] += 1
            grid_cut.append((k, l))
            k += 1
            l -= 1
            
        return grid_cut
    
    def idxToAns(self, idx):
        ans = []
        for i in range(self.n):
            a = ''
            for j in range(self.n):
                if j == idx[i]:
                    a += 'Q'
                else:
                    a += '.'
            ans.append(a)
        return ans