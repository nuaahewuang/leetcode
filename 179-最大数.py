'''
FilePath: 179-最大数.py
Author: Huang_CJ
Date: 2024-05-26 11:05:44
LastEditTime: 2024-05-26 11:23:41
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
'''

'''
示例 1：
输入：nums = [10,2]
输出："210"
示例 2：
输入：nums = [3,30,34,5,9]
输出："9534330"
'''
from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def sort_rule(x, y):
            a, b = x + y, y + x
            if a < b: return 1
            elif a > b: return -1
            else: return 0

        nums_list = [str(num) for num in nums]
        nums_list.sort(key = cmp_to_key(sort_rule))
        #print(nums_list)
        if nums_list[0] == '0':
            return '0'
        else:
            return ''.join(nums_list)

solution = Solution()
solution.largestNumber(nums=[3,30,34,5,9])