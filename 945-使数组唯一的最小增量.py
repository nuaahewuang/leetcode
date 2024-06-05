'''
FilePath: 945-使数组唯一的最小增量.py
Author: Huang_CJ
Date: 2024-06-05 10:31:52
LastEditTime: 2024-06-05 10:35:13
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个整数数组 nums 。每次 move 操作将会选择任意一个满足 0 <= i < nums.length 的下标 i，并将 nums[i] 递增 1。
返回使 nums 中的每个值都变成唯一的所需要的最少操作次数。
'''

'''
示例 2：
输入：nums = [3,2,1,2,1,7]
输出：6
解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
'''

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i - 1]:
                count += nums[i - 1] - nums[i] + 1 
                nums[i] = nums[i - 1] + 1
        return count

'''
核心思想：贪心算法在于每个子问题的局部最优解会指向全局最优解。
显然在对数组排序之后，可以通过保证数组的最后一个元素，经过+1操作后比前面所有元素大即可,此时子问题的最优解会收敛于全局最优解
'''