'''
FilePath: 2154-将找到的值乘以2.py
Author: Huang_CJ
Date: 2024-05-30 19:50:15
LastEditTime: 2024-05-30 19:50:24
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个整数数组 nums ，另给你一个整数 original ，这是需要在 nums 中搜索的第一个数字。
接下来，你需要按下述步骤操作：
如果在 nums 中找到 original ，将 original 乘以 2 ，得到新 original（即，令 original = 2 * original）。
否则，停止这一过程。
只要能在数组中找到新 original ，就对新 original 继续 重复 这一过程。
返回 original 的 最终 值。
'''

class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """

        nums.sort()
        for n in nums:
            if n == original:
                original *= 2
            
        
        return original
