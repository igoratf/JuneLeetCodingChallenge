    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node):
            if not node:
                return
            
            if node.left and node.right:
                left = node.left
                node.left = node.right
                node.right = left
                
                invert(node.left)
                invert(node.right)
            
            elif node.left:
                node.right = node.left
                node.left = None
                invert(node.right)
            
            elif node.right:
                node.left = node.right
                node.right = None
                invert(node.left)
            
            return node
        
        return invert(root)