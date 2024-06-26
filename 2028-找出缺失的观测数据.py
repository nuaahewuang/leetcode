'''
FilePath: 2028-找出缺失的观测数据.py
Author: Huang_CJ
Date: 2024-05-27 11:37:46
LastEditTime: 2024-06-03 14:18:31
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 现有一份 n + m 次投掷单个 六面 骰子的观测数据，骰子的每个面从 1 到 6 编号。观测数据中缺失了 n 份，你手上只拿到剩余 m 次投掷的数据。幸好你有之前计算过的这 n + m 次投掷数据的 平均值 。
给你一个长度为 m 的整数数组 rolls ，其中 rolls[i] 是第 i 次观测的值。同时给你两个整数 mean 和 n 。
返回一个长度为 n 的数组，包含所有缺失的观测数据，且满足这 n + m 次投掷的 平均值 是 mean 。如果存在多组符合要求的答案，只需要返回其中任意一组即可。如果不存在答案，返回一个空数组。
k 个数字的 平均值 为这些数字求和后再除以 k 。
注意 mean 是一个整数，所以 n + m 次投掷的总和需要被 n + m 整除。
'''

'''
示例 1：
输入：rolls = [3,2,4,3], mean = 4, n = 2
输出：[6,6]
解释：所有 n + m 次投掷的平均值是 (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4 。
示例 2：
输入：rolls = [1,5,6], mean = 3, n = 4
输出：[2,3,2,2]
解释：所有 n + m 次投掷的平均值是 (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3 。
'''

class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """

        missingsum = mean * (n + len(rolls)) - sum(rolls)

        if not n <= missingsum <= n * 6:
            return []
        
        quotient , remainder = divmod(missingsum, n)
        return [quotient + 1] * remainder + [quotient] * (n - remainder)

'''
核心思路：由 n 个在 [1,6] 范围内的整数组成且这 n 个整数之和为 missingsum ， 记 quotient = missing / n 的向下取整，remainder = missingsum mod n，则可以构造一种符合要求的答案：在缺失的 nnn 个观测数据中，有 remainder 个观测数据是 quotient+1 ，其余观测数据都是 quotient 。

'''