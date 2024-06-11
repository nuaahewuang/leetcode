'''
FilePath: 2433-找出前缀异或的原始数组.py
Author: Huang_CJ
Date: 2024-06-11 15:27:18
LastEditTime: 2024-06-11 15:30:29
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个长度为 n 的 整数 数组 pref 。找出并返回满足下述条件且长度为 n 的数组 arr ：
pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
注意 ^ 表示 按位异或（bitwise-xor）运算。
可以证明答案是 唯一 的。
'''

'''
示例：
输入：pref = [5,2,0,3,1]
输出：[5,7,2,3,2]
解释：从数组 [5,7,2,3,2] 可以得到如下结果：
- pref[0] = 5
- pref[1] = 5 ^ 7 = 2
- pref[2] = 5 ^ 7 ^ 2 = 0
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1
'''

class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """

        ans = [pref[0]]
        for i in range(1,len(pref)):
            ans.append(pref[i] ^ pref[i-1])
        return ans

'''
核心思路：按位异或的性质：A xor B = C 则 A xor C = B。同时由于前缀在继承：ans[i] = pref[i] ^ pref[i - 1]
'''