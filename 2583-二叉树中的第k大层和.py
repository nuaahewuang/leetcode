'''
FilePath: 2583-二叉树中的第k大层和.py
Author: Huang_CJ
Date: 2024-05-24 11:05:28
LastEditTime: 2024-05-24 11:15:03
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一棵二叉树的根节点 root 和一个正整数 k 。

树中的 层和 是指 同一层 上节点值的总和。

返回树中第 k 大的层和（不一定不同）。如果树少于 k 层，则返回 -1 。

注意，如果两个节点与根节点的距离相同，则认为它们在同一层。
'''

'''
示例1：
输入：root = [5,8,9,2,1,3,7,4,6], k = 2
输出：13
解释：树中每一层的层和分别是：
- Level 1: 5
- Level 2: 8 + 9 = 17
- Level 3: 2 + 1 + 3 + 7 = 13
- Level 4: 4 + 6 = 10
第 2 大的层和等于 13 。
'''

from collections import deque

# 定义二叉树节点
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return -1
        
        # 使用队列进行广度优先搜索
        queue = deque([root])
        level_sums = []

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_sums.append(level_sum)
        
        if len(level_sums) < k:
            return -1
        
        # 对层和进行排序，找到第 k 大的层和
        level_sums.sort(reverse=True)
        return level_sums[k - 1]

'''
核心思想；利用队列实现广度优先算法，队列中存储当前层节点。出队时，计入层和，并且将子结点入队。
'''