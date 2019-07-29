# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:27:14 2019

@author: admin
"""

'''
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def singleNumber(self, nums: list) -> list:
    # def singleNumber(self, nums: List[int]) -> List[int]:
        idxSingle = []
        idxPool = list(range(len(nums)))
        hashNum = len(nums)
        while len(idxSingle) != 2:
            idxSingle = self.hashSearchOneRound(nums, idxPool, hashNum)
            if idxSingle != []:
                idxPool = idxSingle
            else:
                idxPool = list(range(len(nums)))
            hashNum -= 1
        res = [nums[i] for i in idxSingle]
        return res
    
    def hashSearchOneRound(self, nums, idxPool, hashNum):
        for i in idxPool:
            hn = int(nums[i]) % hashNum
            self.nsConverter(nums, hn)
        idxStr = []
        for i in range(len(nums)):
            if 'str' in str(type(nums[i])):
                idxStr.append(i)
                nums[i] = int(nums[i])
               
        idxSingle = []
        for i in idxPool:
            hn = int(nums[i]) % hashNum
            if hn in idxStr:
                idxSingle.append(i)
        return idxSingle
        
            
        
    
    def nsConverter(self, nums, i):
        if 'str' in str(type(nums[i])):
            nums[i] = int(nums[i])
        else:
            nums[i] = str(nums[i])
            
  
        
        
cl = Solution()
nums = [29328859,1466838361,-66079248,926571150,1456000429,926571150,1536309894,-182157937,-391092726,1518731260,-66079248,-1116874613,-1703212692,-1116874613,-1321264512,-816411092,-483719306,110721554,29328859,-357092863,-391092726,-357092863,1466838361,-1703212692,-1321264512,1518731260,1536309894,640411520,-182157937,-816411092,1456000429,-483719306]


res = cl.singleNumber(nums)        
        




