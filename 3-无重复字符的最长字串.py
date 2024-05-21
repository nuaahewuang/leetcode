'''
FilePath: 3-无重复字符的最长字串.py
Author: Huang_CJ
Date: 2024-05-21 22:04:05
LastEditTime: 2024-05-21 22:21:36
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
'''

'''
示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

提示：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 使用字典记录每个字符最后出现的索引
        char_index_map ={} 
        
        max_lenth = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_index_map:
                start = max(start,char_index_map[s[end]] + 1)
            char_index_map[s[end]] = end
            max_lenth = max(max_lenth, end - start + 1)

        return max_lenth


'''
核心思路：
滑动窗口：
* 使用两个指针 start 和 end 来表示当前窗口的左右边界。
* 窗口的大小动态变化使得窗口内始终保持不含重复字符的子串。
哈希表：
* 使用哈希表（字典） char_index_map 来记录每个字符最后一次出现的位置。
* 通过检查哈希表，可以快速判断当前字符是否在当前窗口中已经存在。
'''