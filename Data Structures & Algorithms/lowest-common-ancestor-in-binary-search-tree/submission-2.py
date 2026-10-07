# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # compute the path from root to nodes
        paths = [
            self.computePath(root, p),
            self.computePath(root, q)
        ]
        
        # the last common element is the LCA
        i = 0
        max_len = min(len(paths[0]), len(paths[1]))
        while i < max_len and paths[0][i].val == paths[1][i].val :
            i += 1
        return paths[0][i-1]
    
    def computePath(self, root: TreeNode, n: TreeNode) -> List[TreeNode]:
        path = []
        curr = root
        while curr:
            path.append(curr)
            if n.val > curr.val:
                curr = curr.right
            elif n.val < curr.val:
                curr = curr.left
            else:
                break
        return path
        
        