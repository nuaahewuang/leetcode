'''
FilePath: 2283-判断一个数的数字技术是否等与数位的值.py
Author: Huang_CJ
Date: 2024-06-03 14:14:15
LastEditTime: 2024-06-03 14:28:02
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个下标从 0 开始长度为 n 的字符串 num ，它只包含数字。
如果对于 每个 0 <= i < n 的下标 i ，都满足数位 i 在 num 中出现了 num[i]次，那么请你返回 true ，否则返回 false 。
'''

'''
示例 1：
输入：num = "1210"
输出：true
解释：
num[0] = '1' 。数字 0 在 num 中出现了一次。
num[1] = '2' 。数字 1 在 num 中出现了两次。
num[2] = '1' 。数字 2 在 num 中出现了一次。
num[3] = '0' 。数字 3 在 num 中出现了零次。
"1210" 满足题目要求条件，所以返回 true 。
'''

from collections import Counter
class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num_count = Counter(num)
        for i in range(len(num)):
            if int(num[i]) != num_count.get(str(i),0):
                return False
        
        return True


'''
核心函数：以counts.get(word,0) 为例，counts.get(word,0) 返回字典counts中word元素对应的值，若没有返回默认值（进行初始化）。
'''