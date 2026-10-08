# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        # first go to the smallest element
        while curr:
            stack.append(curr)
            curr = curr.left

        # in order traversal
        while curr or stack and k > 1:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                k -= 1

                curr = node.right 
        ret = stack.pop()
        return ret.val