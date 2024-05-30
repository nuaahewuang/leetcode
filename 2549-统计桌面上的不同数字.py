'''
FilePath: 2549-统计桌面上的不同数字.py
Author: Huang_CJ
Date: 2024-05-30 19:09:02
LastEditTime: 2024-05-30 19:12:26
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个正整数 n ，开始时，它放在桌面上。在 109 天内，每天都要执行下述步骤：
对于出现在桌面上的每个数字 x ，找出符合 1 <= i <= n 且满足 x % i == 1 的所有数字 i 。然后，将这些数字放在桌面上。
返回在 109 天之后，出现在桌面上的 不同 整数的数目。
'''
class Solution(object):
    def distinctIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n-1 if n > 1 else 1


'''
核心思路：由于 n mod (n−1)=1n \bmod (n-1) = 1nmod(n−1)=1 一定满足要求，我们可以从 nnn 开始，不断生成 n−1,n−2,⋯n-1,n-2,\cdotsn−1,n−2,⋯，最后 [2,n][2,n][2,n] 中的数字都会在桌面上，这有 n−1n-1n−1 个。
'''