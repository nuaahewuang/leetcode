'''
FilePath: 232-用栈实现队列.py
Author: Huang_CJ
Date: 2024-05-27 12:04:03
LastEditTime: 2024-05-27 12:36:11
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
实现 MyQueue 类：
void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
说明：
你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
'''


class MyQueue(object):

    def __init__(self):
        self.list1 = []
        self.list2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list1.append(x)


    def pop(self):
        """
        :rtype: int
        """
        while len(self.list1) > 1:
            val = self.list1.pop()
            self.list2.append(val)
        val = self.list1.pop()
        while len(self.list2):
            value = self.list2.pop()
            self.list1.append(value)
        return val

    def peek(self):
        """
        :rtype: int
        """
        while len(self.list1) > 1:
            val = self.list1.pop()
            self.list2.append(val)
        value = self.list1.pop()
        self.list2.append(value)
        while len(self.list2) != 0:
            val = self.list2.pop()
            self.list1.append(val)
        return value
   

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.list1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
