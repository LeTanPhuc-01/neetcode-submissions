# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        stack1, stack2 = [p], [q]
        while stack1 and stack2:
            node1, node2 = stack1.pop(), stack2.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack1.append(node1.left)
            stack1.append(node1.right)   
            stack2.append(node2.left)   
            stack2.append(node2.right)   
            
        return not stack1 and not stack2