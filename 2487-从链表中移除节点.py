'''
FilePath: 2487-从链表中移除节点.py
Author: Huang_CJ
Date: 2024-05-30 14:59:34
LastEditTime: 2024-05-30 15:07:45
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个链表的头节点 head 。
移除每个右侧有一个更大数值的节点。
返回修改后链表的头节点 head 。
'''

'''
示例1：
输入：head = [5,2,13,3,8]
输出：[13,8]
解释：需要移除的节点是 5 ，2 和 3 。
- 节点 13 在节点 5 右侧。
- 节点 13 在节点 2 右侧。
- 节点 8 在节点 3 右侧。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s = []  # 设置栈
        while head is not None:
            s.append(head)
            head = head.next

        while s:
            if head is None or s[-1].val >= head.val:
                s[-1].next = head
                head = s[-1]
            s.pop()
        return head

'''
核心思想：将所有链表节点按照从左到右的顺序压入栈中，同时新链表初始为空，不断从栈中弹出节点，如果节点的值大于等于新链表的表头节点值，那么将该节点插入新链表的表头，否则移除该节点。
'''