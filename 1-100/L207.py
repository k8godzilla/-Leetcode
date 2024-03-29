# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 19:18:34 2019

@author: admin
"""

'''
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0]] 
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 其实很简单  只要知道一门课可以上的条件是他的prerequisite都已经在memo中就行了 剩下的就是dfs


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        p = prerequisites
        
        if p == []:
            return True
        
        self.forward = {}
        self.backward = {}
        for i in range(len(p)):
            l0, l1 = p[i][0], p[i][1]
            try:
                self.forward[l1].add(l0)
            except:
                self.forward[l1] = set([l0])
            try:
                self.backward[l0].add(l1)
            except:
                self.backward[l0] = set([l1])
        
        self.courses1 = set(self.forward.keys())
        self.courses0 = set(self.backward.keys())
        
        self.coursesRoot = self.courses1.difference(self.courses0)
        self.coursesAll = self.courses1.union(self.courses0)
        
        
        
        
        if len(self.coursesRoot) == 0:
            return False
        
        self.courseMemo = set()
        self.courseFrontier =  set()
        for c in self.coursesRoot:
            self.courseFrontier.add(c)
            
        while len(self.courseFrontier) > 0:
            c = self.courseFrontier.pop()
            if self.isValid(c):
                self.courseMemo.add(c)
                if c in self.forward.keys():
                    self.courseFrontier.update(self.forward[c])
                    
        if len(self.courseMemo) == len(self.coursesAll):
            return True
        else:
            return False
        
        
        

    def isValid(self, c):
        if c not in self.backward.keys():
            return True
        return self.backward[c].issubset(self.courseMemo)
        
        
        
        

