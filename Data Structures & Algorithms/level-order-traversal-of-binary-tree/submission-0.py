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
        levels = [[root.val]]

        # check indexing of levels
        while queue:
            node = queue.pop(0)
            d = node[1]
            if len(levels) - 1 <= d:
                    levels.append([])
            if node[0].left:
                queue.append([node[0].left, d + 1])
                levels[d + 1].append(node[0].left.val)
                
            if node[0].right:
                queue.append([node[0].right, d + 1])
                levels[d + 1].append(node[0].right.val)
                
        if not levels[-1]:
            levels.pop()
        return levels
        

        