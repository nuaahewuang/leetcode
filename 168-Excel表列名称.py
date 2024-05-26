'''
FilePath: 168-Excel表列名称.py
Author: Huang_CJ
Date: 2024-05-26 11:32:57
LastEditTime: 2024-05-26 11:44:56
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
例如：
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
'''

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        res = []
        while columnNumber:
            cur = (columnNumber-1) % 26 + 1
            res.append(chr(ord('A') + cur - 1))
            columnNumber = (columnNumber - cur) // 26
        return ''.join(res[::-1])

