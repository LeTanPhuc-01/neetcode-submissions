# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      
       dummy = ListNode(0, head)
       left = dummy
       right = head
       while n > 0:
        right = right.next
        n -= 1
       while right:
        left = left.next
        right = right.next
       left.next = left.next.next
       return dummy.next     

       
       
       
       
       
       
       
       
       
       
       
        # nodes = []
        # curr = head
        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next
        # removeIdx = len(nodes) - n
        # if removeIdx == 0:
        #     return head.next
        # nodes[removeIdx - 1].next = nodes[removeIdx].next

        # return head