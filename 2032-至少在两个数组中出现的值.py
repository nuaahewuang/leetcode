'''
FilePath: 2032-至少在两个数组中出现的值.py
Author: Huang_CJ
Date: 2024-05-30 19:26:58
LastEditTime: 2024-05-30 19:29:11
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你三个整数数组 nums1、nums2 和 nums3 ，请你构造并返回一个 元素各不相同的 数组，且由 至少 在 两个 数组中出现的所有值组成。数组中的元素可以按 任意 顺序排列。
'''

class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """

        n1 = nums1
        n2 = nums2
        n3 = nums3
        res = []

        for i in range(1,101):
            if (i in n1) + (i in n2) + (i in n3) >= 2:
                res.append(i)

        return res