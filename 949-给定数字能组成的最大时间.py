'''
FilePath: 949-给定数字能组成的最大时间.py
Author: Huang_CJ
Date: 2024-06-11 14:46:33
LastEditTime: 2024-06-11 14:58:17
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
24 小时格式为 "HH:MM" ，其中 HH 在 00 到 23 之间，MM 在 00 到 59 之间。最小的 24 小时制时间是 00:00 ，而最大的是 23:59 。从 00:00 （午夜）开始算起，过得越久，时间越大。
以长度为 5 的字符串，按 "HH:MM" 格式返回答案。如果不能确定有效时间，则返回空字符串。
'''

import itertools

class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        
        ans = -1
        for h1,h2,m1,m2 in itertools.permutations(arr):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = hours * 60 + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans :
                ans = time
            
        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""