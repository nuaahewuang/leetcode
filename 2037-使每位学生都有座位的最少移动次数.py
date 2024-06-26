'''
FilePath: 2037-使每位学生都有座位的最少移动次数.py
Author: Huang_CJ
Date: 2024-05-30 19:39:29
LastEditTime: 2024-05-30 19:42:15
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 一个房间里有 n 个座位和 n 名学生，房间用一个数轴表示。给你一个长度为 n 的数组 seats ，其中 seats[i] 是第 i 个座位的位置。同时给你一个长度为 n 的数组 students ，其中 students[j] 是第 j 位学生的位置。
你可以执行以下操作任意次：
增加或者减少第 i 位学生的位置，每次变化量为 1 （也就是将第 i 位学生从位置 x 移动到 x + 1 或者 x - 1）
请你返回使所有学生都有座位坐的 最少移动次数 ，并确保没有两位学生的座位相同。
请注意，初始时有可能有多个座位或者多位学生在 同一 位置。
'''

'''
示例 1：
输入：seats = [3,1,5], students = [2,7,4]
输出：4
解释：学生移动方式如下：
- 第一位学生从位置 2 移动到位置 1 ，移动 1 次。
- 第二位学生从位置 7 移动到位置 5 ，移动 2 次。
- 第三位学生从位置 4 移动到位置 3 ，移动 1 次。
总共 1 + 2 + 1 = 4 次移动。
'''

class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """

        seats.sort()
        students.sort()
        res = 0
        for i in range(len(seats)):
            res += abs(seats[i]- students[i])
    
        return res