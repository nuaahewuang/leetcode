'''
FilePath: 1154-一年中的第几天.py
Author: Huang_CJ
Date: 2024-05-25 21:32:32
LastEditTime: 2024-05-25 21:55:43
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。返回该日期是当年的第几天。
'''


class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """

        month_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        date_list = date.split("-")
        year ,month, day = int(date_list[0]), int(date_list[1]), int(date_list[2])

        days = sum(month_list[:month]) + day

        if (year % 400 == 0 or (year % 4  == 0 and year % 100 != 0) ) and month > 2 :
            days += 1

        return days    

solution = Solution()

print(solution.dayOfYear(date="1900-05-02"))

'''
核心点：闰年的判定方法为—— year 是 400 的倍数，或者 year 是 4 的倍数且不是 100 的倍数。以及闰年月数过 2 月才需加一天
'''