'''
FilePath: 1290-二进制链表转整数.py
Author: Huang_CJ
Date: 2024-06-05 10:13:25
LastEditTime: 2024-06-05 10:16:54
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。
请你返回该链表所表示数字的 十进制值 。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        res = 0
        while cur:
            res = res * 2 + cur.val
            cur = cur.next
        return res