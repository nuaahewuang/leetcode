'''
FilePath: 2575-找出字符串的可整除数组.py
Author: Huang_CJ
Date: 2024-05-25 21:18:55
LastEditTime: 2024-05-25 21:30:06
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个下标从 0 开始的字符串 word ，长度为 n ，由从 0 到 9 的数字组成。另给你一个正整数 m 。
word 的 可整除数组 div  是一个长度为 n 的整数数组，并满足：
如果 word[0,...,i] 所表示的 数值 能被 m 整除，div[i] = 1；否则，div[i] = 0。返回 word 的可整除数组。
'''

'''
示例 1：
输入：word = "998244353", m = 3
输出：[1,1,0,0,0,1,1,0,0]
解释：仅有 4 个前缀可以被 3 整除："9"、"99"、"998244" 和 "9982443" 。
'''

class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        cur = 0
        div = []
        for ch in word:
            cur = (cur *10 + int(ch)) % m
            div.append(1 if cur == 0 else 0)
        return div

solution = Solution()
print(solution.divisibilityArray(word="998244353",m = 3))


'''
核心思想：一个整数可表示为 a×10+ba \times 10 + ba×10+b：
(a×10+b)mod  m=(amod  m×10+b)mod  m(a \times 10 + b) \mod m = (a \mod m \times 10 + b) \mod m
(a×10+b)modm=(amodm×10+b)modm
所以可以按照上面的递推式，根据当前表示整数的余数，算出包含下一位字符所表示的整数的余数。

当余数为零时即为可整除数组，否则不是。最后返回结果即可。

'''