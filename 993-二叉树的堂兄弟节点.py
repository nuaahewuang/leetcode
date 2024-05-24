'''
FilePath: 993-二叉树的堂兄弟节点.py
Author: Huang_CJ
Date: 2024-05-24 11:46:06
LastEditTime: 2024-05-24 12:02:30
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。
只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。
'''

'''
示例1：
输入：root = [1,2,3,4], x = 4, y = 3
输出：false
'''

from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        if not root :
            return False
    
        queue = deque([(root,None)])    # (node, parent)

        while queue:
            size = len(queue)
            x_parent = y_parent = None

            for _ in range(size):
                node, parent = queue.popleft()

                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent
                
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right,node))

            if x_parent and y_parent:
                return x_parent != y_parent
            if x_parent or y_parent:
                return False
                
        return False

'''
核心思想：使用队列进行广度优先遍历，遍历当前层所有结点，检查是否找到了x和y，如果找到了，记录他们的父结点，如果在同一层找到x和y，比较它们的父节点是否不同。如果不同，返回 True；否则，返回 False。比较它们的父节点是否不同。如果不同，返回 True；否则，返回 False。如果遍历完整棵树也没有找到 x 和 y，返回 False。
'''