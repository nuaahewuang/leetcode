'''
FilePath: 2903-找出满足差值条件的下标Ⅰ.py
Author: Huang_CJ
Date: 2024-05-25 20:45:10
LastEditTime: 2024-05-25 21:05:27
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个下标从 0 开始、长度为 n 的整数数组 nums ，以及整数 indexDifference 和整数 valueDifference 。
你的任务是从范围 [0, n - 1] 内找出  2 个满足下述所有条件的下标 i 和 j ：
abs(i - j) >= indexDifference 且
abs(nums[i] - nums[j]) >= valueDifference
返回整数数组 answer。如果存在满足题目要求的两个下标，则 answer = [i, j] ；否则，answer = [-1, -1] 。如果存在多组可供选择的下标对，只需要返回其中任意一组即可。

注意：i 和 j 可能 相等 。
'''

class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j] >= valueDifference):
                    return [i,j]
        return [-1,-1]

nums,  indexDifference,valueDifference  = [5,1,4,1],2, 4

solution = Solution()
print(solution.findIndices(nums,indexDifference,valueDifference))

