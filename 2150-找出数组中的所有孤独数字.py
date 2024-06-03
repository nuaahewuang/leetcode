'''
FilePath: 2150-找出数组中的所有孤独数字.py
Author: Huang_CJ
Date: 2024-06-03 13:27:24
LastEditTime: 2024-06-03 13:36:09
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个整数数组 nums 。如果数字 x 在数组中仅出现 一次 ，且没有 相邻 数字（即，x + 1 和 x - 1）出现在数组中，则认为数字 x 是 孤独数字 。
返回 nums 中的 所有 孤独数字。你可以按 任何顺序 返回答案。
'''

from collections import Counter
class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        freq = Counter(nums)    # 每个元素出现次数的哈希表
        for n in nums:
            if freq[n-1] == 0 and freq[n+1] ==0 and freq[n] == 1:
                res.append(n)

        return res


'''
Count()主要功能：可以支持方便、快速的计数，将元素数量统计，然后计数并返回一个字典，键为元素，值为元素个数。
'''