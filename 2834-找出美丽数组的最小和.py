'''
FilePath: 2834-找出美丽数组的最小和.py
Author: Huang_CJ
Date: 2024-05-30 15:16:00
LastEditTime: 2024-05-30 15:26:16
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你两个正整数：n 和 target 。如果数组 nums 满足下述条件，则称其为 美丽数组 。
nums.length == n. nums 由两两互不相同的正整数组成。
在范围 [0, n-1] 内，不存在 两个 不同 下标 i 和 j ，使得 nums[i] + nums[j] == target 。
返回符合条件的美丽数组所可能具备的 最小 和，并对结果进行取模 10^9 + 7。
'''

'''
示例1：
输入：n = 3, target = 3
输出：8
解释：
nums = [1,3,4] 是美丽数组。 
- nums 的长度为 n = 3 。 
- nums 由两两互不相同的正整数组成。 
- 不存在两个不同下标 i 和 j ，使得 nums[i] + nums[j] == 3 。
可以证明 8 是符合条件的美丽数组所可能具备的最小和。
'''

class Solution(object):
    def minimumPossibleSum(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        m = target // 2
        if n <= m:
            return ((1 + n) * n // 2) % mod
        
        return ((1 + m) * m // 2 + (target * 2 + (n - m) - 1) * (n - m) // 2) % mod


'''
核心思路：根据题意，我们需要构造一个大小为 n 的正整数数组，该数组由不同的数字组成，并且没有任意两个数字的和等于 target，在满足这样的前提下，要保证数组的和最小。
为了让数组之和最小，我们按照1，2，3，……的顺序考虑，但添加了 x 之后就不能添加 target - x ，因此最大可添加到 target // 2 ,如果个数还不够 n 个，就继续从 target,target+1,target+2,……依次添加。由于数字是连续的，所以可以用等差数列求和公式快速求解。
令 m = target // 2, 分情况求解：
若 n <= m, 最小数组和为 n * (n + 1) / 2.
若 n > m, 最小数组和为 m * (1 + m) / 2 + (target + (target + (n-m) -1)) * (n-m) / 2. 
'''