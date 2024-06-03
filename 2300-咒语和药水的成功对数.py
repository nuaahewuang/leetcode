'''
FilePath: 2300-咒语和药水的成功对数.py
Author: Huang_CJ
Date: 2024-06-03 14:02:27
LastEditTime: 2024-06-03 14:12:34
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，其中 spells[i] 表示第 i 个咒语的能量强度，potions[j] 表示第 j 瓶药水的能量强度。
同时给你一个整数 success 。一个咒语和药水的能量强度 相乘 如果 大于等于 success ，那么它们视为一对 成功 的组合。
请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。
'''

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        pairs = []
        potions.sort()          # 药水数目排序
        len_p=len(potions)
        for spell in spells:    # 二分法查找
            left, right= 0, len_p - 1
            mid=left+(right-left) // 2
            while left<=right:  # 最终的:len_p-left
               if spell*potions[mid] >= success:
                   right=mid-1
                   mid=(left+right) // 2
               else:
                   left=mid+1
                   mid=(left+right) // 2
            pairs.append(len_p - left)
        
        return pairs