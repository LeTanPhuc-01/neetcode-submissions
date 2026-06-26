# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p,q)])
        while queue:
            # Take nodes out of queue for comaparison
            node1, node2 = queue.popleft()
            # If we reach the case where both are null that mean they are still equals
            if not node1 and not node2:
                continue
            # Cases that make it not the same tree
            if not node1 or not node2 or node1.val != node2.val:
                return False
            # Update queue after operations
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        return True