# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            np, nq = stack.pop()

            if not np and not nq:
                continue
            if not np or not nq:
                return False
            if np.val != nq.val:
                return False

            stack.append((np.left, nq.left))
            stack.append((np.right, nq.right))

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        if not subRoot:
            return False

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







    
        