# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # bfs where i also store the depth and use it as index of the list where to append things


        queue = [[root, 0]] # [node, depth]
        levels = []

        # check indexing of levels
        while queue:
            node, d = queue.pop(0)

            if len(levels) == d: # first elements processed for that level
                levels.append([])
            levels[d].append(node.val)

            if node.left:
                queue.append([node.left, d + 1])
                
            if node.right:
                queue.append([node.right, d + 1])

        return levels
        

        