'''
FilePath: 2520-统计能整除数字的位数.py
Author: Huang_CJ
Date: 2024-06-11 15:04:43
LastEditTime: 2024-06-11 15:12:04
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个整数 num ，返回 num 中能整除 num 的数位的数目。
如果满足 nums % val == 0 ，则认为整数 val 可以整除 nums 。
'''

class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        num_list = [int(ch) for ch in str(num)]

        #print(num_list)
        count = 0
        for i in num_list:
            if num % i == 0:
                count += 1

        return count 

        
s = Solution()
s.countDigits(num=1248)