'''
FilePath: 2-两数相加.py
Author: Huang_CJ
Date: 2024-05-20 17:14:59
LastEditTime: 2024-05-20 18:07:08
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

提示：
每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def tonum(ll):
            num = 0
            for i in ll:
                num = num * 10 + i
            return num
        
        # 链表转化为列表
        def linked_list_to_list(node):
            lst = []
            while node:
                lst.append(node.val)
                node = node.next
            return lst
        
        # 列表转化为链表
        def list_to_linked_list(lst):
            dummy = ListNode(0)
            current = dummy
            for number in lst:
                current.next = ListNode(number)
                current = current.next
            return dummy.next
        
        # 链表转为逆向列表
        l1_list = linked_list_to_list(l1)[::-1]
        l2_list = linked_list_to_list(l2)[::-1]

        # 列表转化为数字
        num1 = tonum(l1_list)
        num2 = tonum(l2_list)

       
        result_num = num1 + num2

        # 数字转化为列表
        result_list = [int(digit) for digit in str(result_num)][::-1]

        # 列表转化为链表
        return list_to_linked_list(result_list)



def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(result)

# Example usage
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # 输出: [7, 0, 8]


'''
核心思路：整数，列表，链表之间的转化
'''