'''
FilePath: 2085-统计出现过一次的公共给字符串.py
Author: Huang_CJ
Date: 2024-06-03 13:38:45
LastEditTime: 2024-06-03 13:40:58
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你两个字符串数组 words1 和 words2 ，请你返回在两个字符串数组中 都恰好出现一次 的字符串的数目。
'''

from collections import Counter
class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        freq1 = Counter(words1)
        freq2 = Counter(words2)

        res = 0
        for c in freq1:
            if freq1[c] == 1 and freq2[c] == 1:
                res += 1
        return res