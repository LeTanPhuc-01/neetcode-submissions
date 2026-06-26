# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        # Reverse second-half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2














        # if not head: return
        # nodes = []
        # curr = head
        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next
        
        # l, r = 0, len(nodes)-1
        # while l < r:
        #     nodes[l].next = nodes[r]
        #     l += 1
        #     if l == r:
        #         break
        #     nodes[r].next = nodes[l]
        #     r-= 1
        # nodes[l].next = None
        
        