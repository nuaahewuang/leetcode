'''
FilePath: 2129-将标题首字母大写.py
Author: Huang_CJ
Date: 2024-05-24 11:20:38
LastEditTime: 2024-05-24 11:32:48
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个字符串 title ，它由单个空格连接一个或多个单词组成，每个单词都只包含英文字母。请你按以下规则将每个单词的首字母大写 ：
如果单词的长度为 1 或者 2 ，所有字母变成小写。
否则，将单词首字母大写，剩余字母变成小写。
请你返回 大写后 的 title 。
'''

'''
示例 1：
输入：title = "capiTalIze tHe titLe"
输出："Capitalize The Title"
解释：
由于所有单词的长度都至少为 3 ，将每个单词首字母大写，剩余字母变为小写。
示例 2：
输入：title = "First leTTeR of EACH Word"
输出："First Letter of Each Word"
解释：
单词 "of" 长度为 2 ，所以它保持完全小写。
其他单词长度都至少为 3 ，所以其他单词首字母大写，剩余字母小写。
'''

class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        
        title_list = title.split(" ")
        res = []
        for item in title_list:
            if len(item) < 3:
                res.append(item.lower())
            else:
                res.append(item[0].upper() + item[1:].lower())
        return " ".join(res)
            
title = "First leTTeR of EACH Word"
solution = Solution()
print(solution.capitalizeTitle(title))
