# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # No nodes or only one node -> No cycle possible
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            # If fast reaches the end, no cycle
            if not fast or not fast.next:
                return False
            
            slow = slow.next       # Moves 1 step
            fast = fast.next.next  # Moves 2 steps
        
        # If we exit the loop, slow == fast -> cycle found!
        return True