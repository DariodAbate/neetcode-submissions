# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p = self.computePath(root, p)
        path_q = self.computePath(root, q)
        

        lca = root 
        for node_p, node_q in zip(path_p, path_q):
            if node_p.val == node_q.val:
                lca = node_p
            else:
                break
                
        return lca
    
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
        
        