'''
FilePath: 2278-字母在字符串中的百分比.py
Author: Huang_CJ
Date: 2024-06-03 14:55:27
LastEditTime: 2024-06-03 14:58:23
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个字符串 s 和一个字符 letter ，返回在 s 中等于 letter 字符所占的 百分比 ，向下取整到最接近的百分比。
'''

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)
