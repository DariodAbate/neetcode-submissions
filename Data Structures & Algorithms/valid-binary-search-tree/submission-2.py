# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        # each value has a lower and upper bound
        q = deque([[root, float('-inf'), float('inf')]]) 

        while q:
            n, lb, ub = q.popleft()

            if n.val <= lb or n.val >= ub:
                return False
            
            if n.left:
                q.append([n.left, lb, n.val])

            if n.right:
                q.append([n.right, n.val, ub])
        
        return True
        