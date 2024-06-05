'''
FilePath: 937-重新排列日志文件.py
Author: Huang_CJ
Date: 2024-06-05 10:52:01
LastEditTime: 2024-06-05 11:06:07
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个日志数组 logs。每条日志都是以空格分隔的字串，其第一个字为字母与数字混合的 标识符 。
有两种不同类型的日志：
字母日志：除标识符之外，所有字均由小写字母组成
数字日志：除标识符之外，所有字均由数字组成
请按下述规则将日志重新排序：
所有 字母日志 都排在 数字日志 之前。
字母日志 在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序。
数字日志 应该保留原来的相对顺序。
返回日志的最终顺序。
'''

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters = []
        nums = []

        for log in logs:
            logsplit = log.split(" ")
            # print(logsplit)
            if logsplit[1].isalpha():
                letters.append((" ".join(logsplit[1:]),logsplit[0]))
            else:
                nums.append(log)
        
        letters.sort()
        return [letter[1] + " " + letter[0] for letter in letters] + nums

solution = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(solution.reorderLogFiles(logs))


'''
核心思路：用两个列表分别存储字母日志和数字日志，先分别排序，再拼接到一起。
首先分割标识符和内容，如果是内容的第一个单词是英文字符说明是字母日志，放进letters列表，如果是数字字符串，放入nums列表。
注意：对 letters进行排序：因为 元组 里首先是内容，然后是标识符，所以 sort()会先对内容进行排序，然后再对标识符进行排序。
'''