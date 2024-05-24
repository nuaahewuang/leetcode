'''
FilePath: 1673-找出最具竞争力的子序列.py
Author: Huang_CJ
Date: 2024-05-24 10:36:58
LastEditTime: 2024-05-24 10:59:03
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个整数数组 nums 和一个正整数 k ，返回长度为 k 且最具 竞争力 的 nums 子序列。

数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。

在子序列 a 和子序列 b 第一个不相同的位置上，如果 a 中的数字小于 b 中对应的数字，那么我们称子序列 a 比子序列 b（相同长度下）更具 竞争力 。 例如，[1,3,4] 比 [1,3,5] 更具竞争力，在第一个不相同的位置，也就是最后一个位置上， 4 小于 5 。
'''

'''
示例 1：
输入：nums = [3,5,2,6], k = 2
输出：[2,6]
解释：在所有可能的子序列集合 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]} 中，[2,6] 最具竞争力。
示例 2：
输入：nums = [2,4,3,3,5,4,9,6], k = 4
输出：[2,3,3,4]
'''

class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack = []
        drop = len(nums) - k    # 还可以移除的元素数量
        
        for num in nums:
            while stack and drop > 0 and stack[-1] > num:
                stack.pop()
                drop -= 1
            stack.append(num)
        
        return stack[:k]

'''
核心思想：使用一个栈来存储最具竞争力的子序列元素，并在保证最终结果长度为 k 的前提下，尽可能地移除较大的元素
'''