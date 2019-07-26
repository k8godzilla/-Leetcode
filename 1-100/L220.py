# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:07:52 2019

@author: admin
"""

'''
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool:
    # def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) <= 1:
            return False
        
        if k == 0:
            return False
        
        numList = [nums[0]]
        for i in range(1, len(nums)):

     
            

            numList, idxInsert = self.binaryInsert(numList, nums[i])

            if idxInsert == 0:
                if numList[1] - nums[i] <= t:

                    return True
            elif idxInsert == -1:
                if nums[i] - numList[-2] <= t:

                    return True
            else:
                if nums[i] - numList[idxInsert - 1] <= t or numList[idxInsert + 1] - nums[i] <= t:
                    return True
                
            if i - k >= 0:
                self.binaryDelete(numList, nums[i - k])
                
            

        return False
                
            

    def binaryDelete(self, numList, num):
        i, j = 0, len(numList) - 1
        while i <= j:
            if j - i <= 1:
                if numList[j] == num:
                    del numList[j]
                    break
                else:
                    del numList[i]
                    break
            else:
                iM = (i + j) // 2
                if numList[iM] == num:
                    del numList[iM]
                    break
                elif numList[iM] > num:
                    j = iM
                else:
                    i = iM
        
   
    def binaryInsert(self, numList, num):
        if num < numList[0]:
            numList = [num] + numList
            return numList, 0
        elif num >= numList[-1]:
            numList.append(num)
            return numList, -1
        else:
            i, j = 0, len(numList) - 1
            while i <= j:
                if j - i <= 1:
                    if numList[j] <= num:
                        idxInsert = j
                        break
                    else:
                        idxInsert = i
                        break
                iM = (i + j) // 2
                if numList[iM] <= num and numList[iM + 1] >= num:
                    idxInsert = iM
                    break
                elif numList[iM] > num:
                    j = iM
                else:
                    i = iM
            numList = numList[:idxInsert + 1] + [num] + numList[idxInsert + 1:]
        return numList, idxInsert + 1
        
        
        




cl = Solution()
nums = [4,1, 6, 3]
k = 100
t = 1

res = cl.containsNearbyAlmostDuplicate(nums, k, t)


numList, idxInsert = cl.binaryInsert([1, 4, 6], 3)

