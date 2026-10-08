# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs in which i compare the number with the highest for that "search"

        stack = [[root, root.val]]
        gn = 0
        while stack:
            node, max_elem = stack.pop()
            if node.val >= max_elem:
                max_elem = node.val
                gn += 1

            if node.left:
                stack.append([node.left, max_elem])
            if node.right:
                stack.append([node.right, max_elem])

        return gn
        