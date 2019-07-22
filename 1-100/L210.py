# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:32:50 2019

@author: admin
"""

'''
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:

输入: 2, [[1,0]] 
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2:

输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
     因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list) -> list:
        # findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        p = prerequisites
        
        
        if p == []:
            return list(range(n))
        
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
        
        self.coursesTotal = set(list(range(n)))
        self.coursesResid = self.coursesTotal.difference(self.coursesAll)
        
        
        if len(self.coursesRoot) == 0:
            return []
        
        self.courseMemo = set()
        self.courseFrontier =  set()
        self.courseSequence = []
        for c in self.coursesRoot:
            self.courseFrontier.add(c)
            
        while len(self.courseFrontier) > 0:
            c = self.courseFrontier.pop()
            if self.isValid(c):
                self.courseMemo.add(c)
                self.courseSequence.append(c)
                if c in self.forward.keys():
                    self.courseFrontier.update(self.forward[c])
                    
        if len(self.courseMemo) == len(self.coursesAll):
            self.courseSequence.extend(self.coursesResid)
            return self.courseSequence
        else:
            return []
        
        
        

    def isValid(self, c):
        if c not in self.backward.keys():
            return True
        return self.backward[c].issubset(self.courseMemo)
        



