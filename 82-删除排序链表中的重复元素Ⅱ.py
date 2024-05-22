'''
FilePath: 82-删除排序链表中的重复元素Ⅱ.py
Author: Huang_CJ
Date: 2024-05-22 18:16:56
LastEditTime: 2024-05-22 18:35:31
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
'''

'''
示例1：
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
示例2：
输入：head = [1,1,1,2,3]
输出：[2,3]
'''


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        cur = dummy = ListNode(next=head)
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val == val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

'''
核心思想：由于给定的链表是排好序的，因此重复的元素在链表中出现的位置是连续的，因此只需要对链表进行一次遍历，就可以删除重复的元素。由于链表的头节点可能会被删除，因此需要额外使用一个哑节点（dummy node）指向链表的头节点。
'''