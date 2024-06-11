'''
FilePath: 1456-定长子串中元音的最大数目.py
Author: Huang_CJ
Date: 2024-06-11 18:58:53
LastEditTime: 2024-06-11 19:07:27
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你字符串 s 和整数 k 。
请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
英文中的 元音字母 为（a, e, i, o, u）。
'''

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def isVowel(ch):
            return int(ch in "aeiou")
        
        n = len(s)

        count = sum(1 for i in range(k) if isVowel(s[i]))
        maxx = count

        # 滑动窗口 定长为k
        for i in range(k,n):
            count += isVowel(s[i]) - isVowel(s[i-k])
            maxx = max(maxx,count)
        return maxx