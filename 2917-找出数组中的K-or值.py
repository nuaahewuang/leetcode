'''
FilePath: 2917-找出数组中的K-or值.py
Author: Huang_CJ
Date: 2024-05-30 15:54:27
LastEditTime: 2024-05-30 15:57:21
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个整数数组 nums 和一个整数 k 。让我们通过扩展标准的按位或来介绍 K-or 操作。在 K-or 操作中，如果在 nums 中，至少存在 k 个元素的第 i 位值为 1 ，那么 K-or 中的第 i 位的值是 1 。
返回 nums 的 K-or 值。
'''

class Solution(object):
    def findKOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        res = 0
        for i in range(31):
            cnt = sum(1 for num in nums if ((num >> i) & 1) > 0)

            if cnt >= k:
                res |= 1 << i
        return res
