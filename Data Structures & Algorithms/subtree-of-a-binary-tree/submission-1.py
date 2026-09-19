# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right)
            )



        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        if not subRoot:
            return True

        while stack:
            nr = stack.pop()

            if not nr:
                continue

            if nr.val == subRoot.val:
                if self.isSameTree(nr, subRoot):
                    return True
            
            stack.append(nr.left)
            stack.append(nr.right)


        return False







    
        