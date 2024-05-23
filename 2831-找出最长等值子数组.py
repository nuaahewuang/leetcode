'''
FilePath: 2831-找出最长等值子数组.py
Author: Huang_CJ
Date: 2024-05-23 22:44:53
LastEditTime: 2024-05-23 23:33:59
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
如果子数组中所有元素都相等，则认为子数组是一个 等值子数组 。注意，空数组是 等值子数组 。
从 nums 中删除最多 k 个元素后，返回可能的最长等值子数组的长度。
子数组 是数组中一个连续且可能为空的元素序列。
'''

'''
示例 1：
输入：nums = [1,3,2,3,1,3], k = 3
输出：3
解释：最优的方案是删除下标 2 和下标 4 的元素。
删除后，nums 等于 [1, 3, 3, 3] 。
最长等值子数组从 i = 1 开始到 j = 3 结束，长度等于 3 。
示例 2：
输入：nums = [1,1,2,2,1,1], k = 2
输出：4
解释：最优的方案是删除下标 2 和下标 3 的元素。 
删除后，nums 等于 [1, 1, 1, 1] 。 
数组自身就是等值子数组，长度等于 4 。 
'''

class Solution(object):
    def longestEqualSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)  # 记录窗口内每个数字的出现次数
        #max_freq = 0  # 窗口内某个数字的最大出现次数
        left = 0  # 窗口的左边界
        max_length = 0  # 最长等值子数组的长度

        #for right in range(len(nums)):
        for right, x in enumerate(nums):
            print(right,x)
            count[x] += 1
            #max_freq = max(max_freq, count[nums[right]])

            ### 调整窗口的左边界，保证窗口内最多有 k 个不同的元素
            while (right - left + 1) - count[nums[left]] > k:
                count[nums[left]] -= 1
                left += 1

            # 更新最长等值子数组的长度
            max_length = max(max_length, count[nums[right]])

        return max_length

# 示例用法
nums = [1,3,2,3,1,3]
k = 3
solution = Solution()
print(solution.longestEqualSubarray(nums, k))  # 输出: 3


'''
核心思路：滑动窗口，窗口内最多可以有k个不同的元素，通过 while (right - left + 1) - count[nums[left]] > k 判断当前窗口是否满足条件。如果当前窗口的长度减去窗口内某个数字的最大出现次数大于 k，则需要收缩窗口的左边界。在 while 循环中，减少 count[nums[left]] 的计数，并将左边界 left 右移。
'''
