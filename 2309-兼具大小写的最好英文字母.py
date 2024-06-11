'''
FilePath: 2309-兼具大小写的最好英文字母.py
Author: Huang_CJ
Date: 2024-06-11 18:34:28
LastEditTime: 2024-06-11 18:37:24
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个由英文字母组成的字符串 s ，请你找出并返回 s 中的 最好 英文字母。返回的字母必须为大写形式。如果不存在满足条件的字母，则返回一个空字符串。
最好 英文字母的大写和小写形式必须 都 在 s 中出现。
英文字母 b 比另一个英文字母 a 更好 的前提是：英文字母表中，b 在 a 之 后 出现。
'''

class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = set(s)
        for lower ,upper in zip(reversed(ascii_lowercase),reversed(ascii_uppercase)):
            if lower in s and upper in s:
                return upper
        return ""
