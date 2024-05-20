'''
FilePath: 1-两数之和.py
Author: Huang_CJ
Date: 2024-05-20 16:41:05
LastEditTime: 2024-05-20 17:50:50
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
 
提示：
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案

'''

def twoSum(nums, target):

    # 创建一个哈希表来存储数值及其对应的索引
    num_to_index = {}
    
    # 遍历数组
    for i, num in enumerate(nums):
    # 计算需要的补数
        complement = target - num
        
    # 检查补数是否在哈希表中
        if complement in num_to_index:
        # 如果找到，则返回补数的索引和当前数的索引
            return [num_to_index[complement], i]
        
    # 如果没有找到，将当前数和索引存入哈希表
        num_to_index[num] = i

nums = [3,3]
target = 6

print(twoSum(nums,target))

'''
核心思路：使用哈希表，可以在一次遍历中找到答案。
核心函数：enumerate()，会返回一个迭代器，每次迭代返回一个包含两个元素的元组，第一个元素是索引，第二个元素是对应的值。
'''