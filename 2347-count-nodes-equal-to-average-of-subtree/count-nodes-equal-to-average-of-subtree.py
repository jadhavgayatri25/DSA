# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        matching_nodes_count = 0
        
        def dfs(node):
            nonlocal matching_nodes_count
            
            if not node:
                return 0, 0  # (sum, count)
            
            # Post-order traversal: compute values for left and right subtrees
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Calculate current node's subtree total sum and total node count
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            
            # Integer division performs automatic floor/truncation towards zero
            if total_sum // total_count == node.val:
                matching_nodes_count += 1
                
            return total_sum, total_count
        
        dfs(root)
        return matching_nodes_count