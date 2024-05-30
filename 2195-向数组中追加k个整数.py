'''
FilePath: 2195-向数组中追加k个整数.py
Author: Huang_CJ
Date: 2024-05-30 19:54:54
LastEditTime: 2024-05-30 20:19:26
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个整数数组 nums 和一个整数 k 。请你向 nums 中追加 k 个 未 出现在 nums 中的、互不相同 的 正 整数，并使结果数组的元素和 最小 。
返回追加到 nums 中的 k 个整数之和。
'''


class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()
        start = 0
        res = 0

        for n in nums:
            if k == 0:
                return res
            gap = n - start
            if gap > 1:
                cnt = min(k,gap-1)
                res += (start + 1 + start + cnt) * cnt / 2
                k -= cnt
            start = n
        return res + (2*nums[-1] + k + 1) * k / 2


'''
核心思路：将nums排序，遍历数组nums。求每个两个数字之间可插入的正整数的个数（对于数组的第一个数字，考虑它和0之间的间隙），用等差数列的求和公式计算插入的这些数字总和（应当从间隙的左侧开始计数）
注意，每次插入时，需计算这个间隙可插入的数字的个数gap-1 与 k 两者的最小值 cnt，该值代表着这一步中实际应该插入的数字的个数，并且这一步插入了多少个数字,就从k中减去多少个。

如果k已经为0，那么停止遍历，返回ans即可。如果遍历了nums之后，k仍然没有归0，则意味着还需要将k(当前值)个数字插到数组nums的末尾，使用等差数列求和公式即可
'''