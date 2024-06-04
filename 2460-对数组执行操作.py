'''
FilePath: 2460-对数组执行操作.py
Author: Huang_CJ
Date: 2024-06-04 22:48:19
LastEditTime: 2024-06-04 23:04:21
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个下标从 0 开始的数组 nums ，数组大小为 n ，且由 非负 整数组成。
你需要对数组执行 n - 1 步操作，其中第 i 步操作（从 0 开始计数）要求对 nums 中第 i 个元素执行下述指令：
如果 nums[i] == nums[i + 1] ，则 nums[i] 的值变成原来的 2 倍，nums[i + 1] 的值变成 0 。否则，跳过这步操作。
在执行完 全部 操作后，将所有 0 移动 到数组的 末尾 。
例如，数组 [1,0,2,0,0,1] 将所有 0 移动到末尾后变为 [1,2,1,0,0,0] 。
返回结果数组。
'''

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if i + 1 < nums and nums[i] == nums[i + 1] :
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] != 0:
                nums[i], nums[j] = nums[j] , nums [i]
                j += 1
        return nums      